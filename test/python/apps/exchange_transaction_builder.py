from base64 import urlsafe_b64encode
from typing import Optional, Dict, Callable, Iterable
from enum import Enum, auto, IntEnum
from dataclasses import dataclass

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature

from .pb.exchange_pb2 import NewFundResponse, NewSellResponse, NewTransactionResponse
from .signing_authority import SigningAuthority

class SignatureComputation(Enum):
    BINARY_ENCODED_PAYLOAD   = auto()
    # For SELL and FUND subcommand, prefix sign payload by a '.'
    DOT_PREFIXED_BASE_64_URL = auto()


class SignatureEncoding(Enum):
    DER       = auto()
    # For SELL subcommand, convert DER encoding to plain r,s
    PLAIN_R_S = auto()


class PayloadEncoding(Enum):
    BYTES_ARRAY = auto()
    BASE_64_URL = auto()


class SubCommand(IntEnum):
    SWAP = 0x00
    SELL = 0x01
    FUND = 0x02


SUBCOMMAND_TO_CURVE = {
    SubCommand.SWAP: ec.SECP256K1(),
    SubCommand.SELL: ec.SECP256R1(),
    SubCommand.FUND: ec.SECP256R1(),
}


def get_partner_curve(sub_command: SubCommand) -> ec.EllipticCurve:
    return SUBCOMMAND_TO_CURVE[sub_command]

@dataclass(frozen=True)
class SubCommandSpecs:
    signature_computation: SignatureComputation
    signature_encoding: SignatureEncoding
    payload_encoding: PayloadEncoding
    transaction_type: Callable
    required_fields: Iterable[str]
    payout_field: str
    refund_field: Optional[str]

    def check_conf(self, conf: Dict) -> bool:
        return (all(i in conf for i in self.required_fields) and (len(conf) == len(self.required_fields)))

    def format_transaction(self, transaction: bytes) -> bytes:
        if self.signature_computation == SignatureComputation.DOT_PREFIXED_BASE_64_URL:
            return b"." + transaction
        else:
            return transaction

    def encode_payload(self, raw_transaction: bytes) -> bytes:
        if self.payload_encoding == PayloadEncoding.BASE_64_URL:
            return urlsafe_b64encode(raw_transaction)
        else:
            return raw_transaction

    def encode_signature(self, signature_to_encode: bytes) -> bytes:
        if self.signature_encoding == SignatureEncoding.PLAIN_R_S:
            r, s = decode_dss_signature(signature_to_encode)
            signature_to_encode = r.to_bytes(32, "big") + s.to_bytes(32, "big")
        return signature_to_encode

    def create_transaction(self, conf: Dict, transaction_id: bytes) -> bytes:
        raw_transaction = self.transaction_type(**conf, device_transaction_id=transaction_id).SerializeToString()
        return self.encode_payload(raw_transaction)


SWAP_SPECS: SubCommandSpecs = SubCommandSpecs(
    signature_computation = SignatureComputation.BINARY_ENCODED_PAYLOAD,
    signature_encoding = SignatureEncoding.DER,
    payload_encoding = PayloadEncoding.BYTES_ARRAY,
    transaction_type = NewTransactionResponse,
    required_fields = ["payin_address", "payin_extra_id", "refund_address", "refund_extra_id",
                      "payout_address", "payout_extra_id", "currency_from", "currency_to",
                      "amount_to_provider", "amount_to_wallet"],
    payout_field= "currency_to",
    refund_field= "currency_from"
)

SELL_SPECS: SubCommandSpecs = SubCommandSpecs(
    signature_computation = SignatureComputation.DOT_PREFIXED_BASE_64_URL,
    signature_encoding = SignatureEncoding.PLAIN_R_S,
    payload_encoding = PayloadEncoding.BASE_64_URL,
    transaction_type = NewSellResponse,
    required_fields = ["trader_email", "in_currency", "in_amount", "in_address", "out_currency", "out_amount"],
    payout_field="in_currency",
    refund_field= None
)

FUND_SPECS: SubCommandSpecs = SubCommandSpecs(
    signature_computation = SignatureComputation.DOT_PREFIXED_BASE_64_URL,
    signature_encoding = SignatureEncoding.DER,
    payload_encoding = PayloadEncoding.BASE_64_URL,
    transaction_type = NewFundResponse,
    required_fields = ["user_id", "account_name", "in_currency", "in_amount", "in_address"],
    payout_field="in_currency",
    refund_field= None
)

SUBCOMMAND_TO_SPECS = {
    SubCommand.SWAP: SWAP_SPECS,
    SubCommand.SELL: SELL_SPECS,
    SubCommand.FUND: FUND_SPECS,
}

def craft_tx(subcommand: SubCommand, conf: Dict, transaction_id: bytes) -> bytes:
    subcommand_specs = SUBCOMMAND_TO_SPECS[subcommand]
    assert subcommand_specs.check_conf(conf)
    return subcommand_specs.create_transaction(conf, transaction_id)

def encode_tx(subcommand: SubCommand, signer: SigningAuthority, tx: bytes) -> bytes:
    subcommand_specs = SUBCOMMAND_TO_SPECS[subcommand]
    formated_transaction = subcommand_specs.format_transaction(tx)
    signed_transaction = signer.sign(formated_transaction)
    return subcommand_specs.encode_signature(signed_transaction)

def extract_payout_ticker(subcommand: SubCommand, tx_infos: Dict) -> str:
    subcommand_specs = SUBCOMMAND_TO_SPECS[subcommand]
    return tx_infos[subcommand_specs.payout_field]

def extract_refund_ticker(subcommand: SubCommand, tx_infos: Dict) -> Optional[str]:
    subcommand_specs = SUBCOMMAND_TO_SPECS[subcommand]
    if subcommand_specs.refund_field:
        return tx_infos[subcommand_specs.refund_field]
    else:
        return None