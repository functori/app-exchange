from base64 import urlsafe_b64encode
from contextlib import contextmanager
from typing import Generator, Optional, Dict

from ecdsa import SigningKey, SECP256k1, NIST256p as SECP256r1
from ecdsa.util import sigencode_der
from hashlib import sha256
from ragger.backend.interface import BackendInterface, RAPDU
from ragger import ApplicationError

from ..common import Keys, PARTNER_KEYS, SWAP_PARTNER_KEYS
from .ethereum import ETH_PACKED_DERIVATION_PATH, ETH_CONF, ETH_CONF_DER_SIGNATURE
from .litecoin import LTC_PACKED_DERIVATION_PATH, LTC_CONF, LTC_CONF_DER_SIGNATURE
from .bitcoin import BTC_PACKED_DERIVATION_PATH, BTC_CONF, BTC_CONF_DER_SIGNATURE
from .pb.exchange_pb2 import NewFundResponse, NewSellResponse, NewTransactionResponse
from ..utils import concatenate


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


ERRORS = (
    ApplicationError(0x6A80, "INCORRECT_COMMAND_DATA"),
    ApplicationError(0x6A81, "DESERIALIZATION_FAILED"),
    ApplicationError(0x6A82, "WRONG_TRANSACTION_ID"),
    ApplicationError(0x6A83, "INVALID_ADDRESS"),
    ApplicationError(0x6A84, "USER_REFUSED"),
    ApplicationError(0x6A85, "INTERNAL_ERROR"),
    ApplicationError(0x6A86, "WRONG_P1"),
    ApplicationError(0x6A87, "WRONG_P2"),
    ApplicationError(0x6E00, "CLASS_NOT_SUPPORTED"),
    ApplicationError(0x6D00, "INVALID_INSTRUCTION"),
    ApplicationError(0x9D1A, "SIGN_VERIFICATION_FAIL")
)


class ExchangeClient:
    CLA = 0xE0
    def __init__(self,
                 client: BackendInterface,
                 rate: bytes,
                 subcommand: bytes,
                 partner_keys: Optional[Keys] = None):
        self._rate = rate
        self._subcommand = subcommand
        self._client = client
        self._transaction_id: Optional[bytes] = None
        self._transaction: bytes = b""
        self._payout_payload: bytes = b""
        self._refund_payload: bytes = b""
        if partner_keys:
            self._partner_keys = partner_keys
        elif self._subcommand == SubCommand.SWAP:
            self._partner_keys = SWAP_PARTNER_KEYS
        else:
            self._partner_keys = PARTNER_KEYS
        if self._subcommand in [SubCommand.FUND, SubCommand.SELL]:
            self._key = SigningKey.from_string(self._partner_keys.private, curve=SECP256r1)
        elif self._subcommand == SubCommand.SWAP:
            self._key = SigningKey.from_string(self._partner_keys.private, curve=SECP256k1)

    @property
    def rate(self) -> bytes:
        return self._rate

    @property
    def subcommand(self) -> bytes:
        return self._subcommand

    @property
    def key(self) -> SigningKey:
        return self._key

    @property
    def transaction_id(self) -> bytes:
        return self._transaction_id or b""

    def _exchange(self, ins: int, payload: bytes = b"") -> RAPDU:
        return self._client.exchange(self.CLA, ins, p1=self.rate,
                                     p2=self.subcommand, data=payload)

    @contextmanager
    def _exchange_async(self, ins: int, payload: bytes = b"") -> Generator[RAPDU, None, None]:
        with self._client.exchange_async(self.CLA, ins, p1=self.rate,
                                         p2=self.subcommand, data=payload) as response:
            yield response

    def get_version(self) -> RAPDU:
        return self._exchange(Command.GET_VERSION)

    def init_transaction(self) -> RAPDU:
        response = self._exchange(Command.START_NEW_TRANSACTION)
        self._transaction_id = response.data
        return response

    def set_partner_key(self, pubkey: Optional[bytes] = None) -> RAPDU:
        return self._exchange(Command.SET_PARTNER_KEY,
                              payload=pubkey or self._partner_keys.public)

    def check_partner_key(self, signature: Optional[bytes] = None) -> RAPDU:
        return self._exchange(Command.CHECK_PARTNER,
                              payload=signature or self._partner_keys.signature)

    def _ticker_to_coin_payload(self, ticker) -> bytes:
        ticker_to_conf = {
            "ETH": (ETH_CONF, ETH_CONF_DER_SIGNATURE, ETH_PACKED_DERIVATION_PATH),
            "BTC": (BTC_CONF, BTC_CONF_DER_SIGNATURE, BTC_PACKED_DERIVATION_PATH),
            "LTC": (LTC_CONF, LTC_CONF_DER_SIGNATURE, LTC_PACKED_DERIVATION_PATH),
        }
        assert ticker in ticker_to_conf
        conf, signature, derivation_path = ticker_to_conf[ticker]
        return concatenate(conf) + signature + concatenate(derivation_path)


    def _process_transaction_payload_fund(self, infos: Dict) -> bytes:
        fields = ["user_id", "account_name", "in_currency", "in_amount", "in_address"]
        assert all(i in infos for i in fields)
        assert len(infos) == len(fields)
        pb_buffer = NewFundResponse(**infos, device_transaction_id=self.transaction_id)
        # preparing payload for further check step
        self._payout_payload = self._ticker_to_coin_payload(infos["in_currency"])

        return urlsafe_b64encode(pb_buffer.SerializeToString())

    def _process_transaction_payload_sell(self, infos: Dict) -> bytes:
        fields = ["trader_email", "in_currency", "in_amount", "in_address",
                  "out_currency", "out_amount"]
        assert all(i in infos for i in fields)
        assert len(infos) == len(fields)
        pb_buffer = NewSellResponse(**infos, device_transaction_id=self.transaction_id)
        # preparing payload for further check step
        self._payout_payload = self._ticker_to_coin_payload(infos["in_currency"])
        return urlsafe_b64encode(pb_buffer.SerializeToString())

    def _process_transaction_payload_swap(self, infos: Dict) -> bytes:
        fields = ["payin_address", "payin_extra_id", "refund_address", "refund_extra_id",
                  "payout_address", "payout_extra_id", "currency_from", "currency_to",
                  "amount_to_provider", "amount_to_wallet"]
        assert all(i in infos for i in fields)
        assert len(infos) == len(fields)
        pb_buffer = NewTransactionResponse(
            **infos,
            device_transaction_id=self.transaction_id.decode("utf-8")
        )
        # preparing payload for further check step
        self._payout_payload = self._ticker_to_coin_payload(infos["currency_to"])
        self._refund_payload = self._ticker_to_coin_payload(infos["currency_from"])

        return pb_buffer.SerializeToString()

    def process_transaction(self, infos: Dict, fees: bytes) -> RAPDU:
        if self._subcommand == SubCommand.FUND:
            self._transaction = self._process_transaction_payload_fund(infos)
        elif self._subcommand == SubCommand.SELL:
            self._transaction = self._process_transaction_payload_sell(infos)
        elif self._subcommand == SubCommand.SWAP:
            self._transaction = self._process_transaction_payload_swap(infos)
        else:
            raise NotImplementedError()
        payload = concatenate(self._transaction, fees)
        return self._exchange(Command.PROCESS_TRANSACTION_RESPONSE, payload=payload)

    def check_transaction(self) -> RAPDU:
        # preparing payload to sign
        if self._subcommand in [SubCommand.FUND, SubCommand.SELL]:
            payload_to_sign = b"." + self._transaction
        elif self._subcommand == SubCommand.SWAP:
            payload_to_sign = self._transaction
        # signing payload
        if self._subcommand in [SubCommand.FUND, SubCommand.SWAP]:
            encode_func = sigencode_der
        elif self._subcommand == SubCommand.SELL:
            encode_func = lambda r, s, order: \
                r.to_bytes(32, byteorder="big") + s.to_bytes(32, byteorder="big")
        else:
            raise NotImplementedError()
        signature = self.key.sign(payload_to_sign, hashfunc=sha256, sigencode=encode_func)
        return self._exchange(Command.CHECK_TRANSACTION_SIGNATURE, payload=signature)

    def check_address(self, right_clicks: int, accept: bool = True) -> None:
        if self._subcommand in [SubCommand.SELL, SubCommand.FUND]:
            command = Command.CHECK_PAYOUT_ADDRESS
            payload = self._payout_payload
        elif self._subcommand == SubCommand.SWAP:
            self._exchange(Command.CHECK_PAYOUT_ADDRESS, payload=self._payout_payload)
            command = Command.CHECK_REFUND_ADDRESS
            payload = self._refund_payload
        else:
            raise NotImplementedError()
        with self._exchange_async(command, payload=payload):
            for _ in range(right_clicks):
                self._client.right_click()
            if not accept:
                self._client.right_click()
            self._client.both_click()

    def start_signing_transaction(self) -> RAPDU:
        self._exchange(Command.START_SIGNING_TRANSACTION)
