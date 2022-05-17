from base64 import urlsafe_b64encode
from contextlib import contextmanager

from ecdsa import SigningKey, NIST256p as SECP256r1
from ecdsa.util import sigencode_der
from hashlib import sha256

from .pb.exchange_pb2 import NewFundResponse
from .ethereum import ETH_PACKED_DERIVATION_PATH


class Command:
    GET_VERSION = 0x02
    START_NEW_TRANSACTION = 0x03
    SET_PARTNER_KEY = 0x04
    CHECK_PARTNER = 0x05
    PROCESS_TRANSACTION_RESPONSE = 0x06
    CHECK_TRANSACTION_SIGNATURE = 0x07
    CHECK_PAYOUT_ADDRESS = 0x08
    CHECK_REFUND_ADDRESS = 0x09
    START_SIGNING_TRANSACTION = 0x0A


class SubCommand:
    SWAP = 0x00
    SELL = 0x01
    FUND = 0x02


class Rate:
    FIXED = 0x00
    FLOATING = 0x01


ERRORS = {
    0x6A80: 'INCORRECT_COMMAND_DATA',
    0x6A81: 'DESERIALIZATION_FAILED',
    0x6A82: 'WRONG_TRANSACTION_ID',
    0x6A83: 'INVALID_ADDRESS',
    0x6A84: 'USER_REFUSED',
    0x6A85: 'INTERNAL_ERROR',
    0x6A86: 'WRONG_P1',
    0x6A87: 'WRONG_P2',
    0x6E00: 'CLASS_NOT_SUPPORTED',
    0x6D00: 'INVALID_INSTRUCTION',
    0x9D1A: 'SIGN_VERIFICATION_FAIL'
}

ETH_CONF = bytes([
    0x03, 0x45, 0x54, 0x48, 0x08, 0x45, 0x74, 0x68, 0x65, 0x72, 0x65, 0x75,
    0x6D, 0x05, 0x03, 0x45, 0x54, 0x48, 0x12
])

ETH_CONFIG_SIGNATURE_DER = bytes([
    0x30, 0x44, 0x02, 0x20, 0x65, 0xD7, 0x93, 0x1A, 0xB3, 0x14, 0x43, 0x62,
    0xD5, 0x7E, 0x3F, 0xDC, 0xC5, 0xDE, 0x92, 0x1F, 0xB6, 0x50, 0x24, 0x73,
    0x7D, 0x91, 0x7F, 0x0A, 0xB1, 0xF8, 0xB1, 0x73, 0xD1, 0xED, 0x3C, 0x2E,
    0x02, 0x20, 0x27, 0x49, 0x35, 0x68, 0xD1, 0x12, 0xDC, 0x53, 0xC7, 0x17,
    0x7F, 0x8E, 0x5F, 0xC9, 0x15, 0xD9, 0x1A, 0x90, 0x37, 0x80, 0xA0, 0x67,
    0xBA, 0xDF, 0x10, 0x90, 0x85, 0xA7, 0x3D, 0x36, 0x03, 0x23
])


def concatenate(*args):
    result = b''
    for arg in args:
        result += (bytes([len(arg)]) + arg)
    return result


class ExchangeClient:
    CLA = 0xE0
    def __init__(self, client, rate, subcommand, partner_keys=None):
        self._rate = rate
        self._subcommand = subcommand
        self._client = client
        self._transaction_id = None
        self._transaction = None
        self._partner_keys = partner_keys or (None, None, None)

    @property
    def rate(self):
        return self._rate

    @property
    def subcommand(self):
        return self._subcommand

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def client(self):
        return self._client

    @property
    def transaction(self):
        return self._transaction

    @property
    def partner_priv_key(self):
        return self._partner_keys[0]

    @property
    def partner_pub_key(self):
        return self._partner_keys[1]

    @property
    def partner_key_sig(self):
        return self._partner_keys[2]

    def _exchange(self, ins, payload=b''):
        return self.client.exchange(self.CLA, ins, p1=self.rate, p2=self.subcommand, data=payload).data

    @contextmanager
    def _exchange_async(self, ins, payload=b''):
        with self.client.exchange_async(self.CLA, ins, p1=self.rate, p2=self.subcommand, data=payload) as response:
            yield response

    def get_version(self):
        return self._exchange(Command.GET_VERSION)

    def init_transaction(self):
        self._transaction_id = self._exchange(Command.START_NEW_TRANSACTION)
        return self.transaction_id

    def set_partner_key(self, pubkey=None):
        return self._exchange(Command.SET_PARTNER_KEY, payload=pubkey or self.partner_pub_key)

    def check_partner_key(self, signature=None):
        return self._exchange(Command.CHECK_PARTNER, payload=signature or self.partner_key_sig)

    def process_transaction(self, infos: dict, fees: bytes):
        if self._subcommand == SubCommand.FUND:
            fields = ['user_id', 'account_name', 'in_currency', 'in_amount', 'in_address']
            assert all(i in infos for i in fields)
            assert len(infos) == len(fields)
            pb_buffer = NewFundResponse(**infos, device_transaction_id=self.transaction_id).SerializeToString()
            self._transaction = urlsafe_b64encode(pb_buffer)
        payload = concatenate(self.transaction, fees)
        return self._exchange(Command.PROCESS_TRANSACTION_RESPONSE, payload=payload)

    def check_transaction(self):
        enc_transaction = b'.' + self.transaction
        key = SigningKey.from_string(self.partner_priv_key, curve=SECP256r1)
        signature = key.sign(enc_transaction, hashfunc=sha256, sigencode=sigencode_der)
        return self._exchange(Command.CHECK_TRANSACTION_SIGNATURE, payload=signature)

    def check_address(self, right_clicks: int, accept=True):
        payload = concatenate(ETH_CONF) + ETH_CONFIG_SIGNATURE_DER + concatenate(ETH_PACKED_DERIVATION_PATH)
        with self._exchange_async(Command.CHECK_PAYOUT_ADDRESS, payload=payload):
            for _ in range(right_clicks):
                self.client.right_click()
            if not accept:
                self.client.right_click()
            self.client.both_click()

    def start_signing_transaction(self):
        self._exchange(Command.START_SIGNING_TRANSACTION)