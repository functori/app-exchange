# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/Tron.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63ore/Tron.proto\x12\x08protocol\x1a\x19google/protobuf/any.proto\"\xb9\x01\n\x08\x45xchange\x12\x13\n\x0b\x65xchange_id\x18\x01 \x01(\x03\x12\x17\n\x0f\x63reator_address\x18\x02 \x01(\x0c\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\x03\x12\x16\n\x0e\x66irst_token_id\x18\x06 \x01(\x0c\x12\x1b\n\x13\x66irst_token_balance\x18\x07 \x01(\x03\x12\x17\n\x0fsecond_token_id\x18\x08 \x01(\x0c\x12\x1c\n\x14second_token_balance\x18\t \x01(\x03\"*\n\tAccountId\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\"J\n\tauthority\x12$\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x13.protocol.AccountId\x12\x17\n\x0fpermission_name\x18\x02 \x01(\x0c\"\xed\x11\n\x0bTransaction\x12+\n\x08raw_data\x18\x01 \x01(\x0b\x32\x19.protocol.Transaction.raw\x12\x11\n\tsignature\x18\x02 \x03(\x0c\x12)\n\x03ret\x18\x05 \x03(\x0b\x32\x1c.protocol.Transaction.Result\x1a\xbd\t\n\x08\x43ontract\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32+.protocol.Transaction.Contract.ContractType\x12\'\n\tparameter\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x10\n\x08provider\x18\x03 \x01(\x0c\x12\x14\n\x0c\x43ontractName\x18\x04 \x01(\x0c\x12\x15\n\rPermission_id\x18\x05 \x01(\x05\"\x8d\x08\n\x0c\x43ontractType\x12\x19\n\x15\x41\x63\x63ountCreateContract\x10\x00\x12\x14\n\x10TransferContract\x10\x01\x12\x19\n\x15TransferAssetContract\x10\x02\x12\x15\n\x11VoteAssetContract\x10\x03\x12\x17\n\x13VoteWitnessContract\x10\x04\x12\x19\n\x15WitnessCreateContract\x10\x05\x12\x16\n\x12\x41ssetIssueContract\x10\x06\x12\x19\n\x15WitnessUpdateContract\x10\x08\x12!\n\x1dParticipateAssetIssueContract\x10\t\x12\x19\n\x15\x41\x63\x63ountUpdateContract\x10\n\x12\x19\n\x15\x46reezeBalanceContract\x10\x0b\x12\x1b\n\x17UnfreezeBalanceContract\x10\x0c\x12\x1b\n\x17WithdrawBalanceContract\x10\r\x12\x19\n\x15UnfreezeAssetContract\x10\x0e\x12\x17\n\x13UpdateAssetContract\x10\x0f\x12\x1a\n\x16ProposalCreateContract\x10\x10\x12\x1b\n\x17ProposalApproveContract\x10\x11\x12\x1a\n\x16ProposalDeleteContract\x10\x12\x12\x18\n\x14SetAccountIdContract\x10\x13\x12\x12\n\x0e\x43ustomContract\x10\x14\x12\x17\n\x13\x43reateSmartContract\x10\x1e\x12\x18\n\x14TriggerSmartContract\x10\x1f\x12\x0f\n\x0bGetContract\x10 \x12\x19\n\x15UpdateSettingContract\x10!\x12\x1a\n\x16\x45xchangeCreateContract\x10)\x12\x1a\n\x16\x45xchangeInjectContract\x10*\x12\x1c\n\x18\x45xchangeWithdrawContract\x10+\x12\x1f\n\x1b\x45xchangeTransactionContract\x10,\x12\x1d\n\x19UpdateEnergyLimitContract\x10-\x12#\n\x1f\x41\x63\x63ountPermissionUpdateContract\x10.\x12\x14\n\x10\x43learABIContract\x10\x30\x12\x1b\n\x17UpdateBrokerageContract\x10\x31\x12\x1b\n\x17\x46reezeBalanceV2Contract\x10\x36\x12\x1d\n\x19UnfreezeBalanceV2Contract\x10\x37\x12\"\n\x1eWithdrawExpireUnfreezeContract\x10\x38\x12\x1c\n\x18\x44\x65legateResourceContract\x10\x39\x12\x1e\n\x1aUnDelegateResourceContract\x10:\x1a\xac\x05\n\x06Result\x12\x0b\n\x03\x66\x65\x65\x18\x01 \x01(\x03\x12.\n\x03ret\x18\x02 \x01(\x0e\x32!.protocol.Transaction.Result.code\x12@\n\x0b\x63ontractRet\x18\x03 \x01(\x0e\x32+.protocol.Transaction.Result.contractResult\x12\x14\n\x0c\x61ssetIssueID\x18\x0e \x01(\t\x12\x17\n\x0fwithdraw_amount\x18\x0f \x01(\x03\x12\x17\n\x0funfreeze_amount\x18\x10 \x01(\x03\x12 \n\x18\x65xchange_received_amount\x18\x12 \x01(\x03\x12&\n\x1e\x65xchange_inject_another_amount\x18\x13 \x01(\x03\x12(\n exchange_withdraw_another_amount\x18\x14 \x01(\x03\x12\x13\n\x0b\x65xchange_id\x18\x15 \x01(\x03\"\x1e\n\x04\x63ode\x12\n\n\x06SUCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"\xb1\x02\n\x0e\x63ontractResult\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\n\n\x06REVERT\x10\x02\x12\x18\n\x14\x42\x41\x44_JUMP_DESTINATION\x10\x03\x12\x11\n\rOUT_OF_MEMORY\x10\x04\x12\x18\n\x14PRECOMPILED_CONTRACT\x10\x05\x12\x13\n\x0fSTACK_TOO_SMALL\x10\x06\x12\x13\n\x0fSTACK_TOO_LARGE\x10\x07\x12\x15\n\x11ILLEGAL_OPERATION\x10\x08\x12\x12\n\x0eSTACK_OVERFLOW\x10\t\x12\x11\n\rOUT_OF_ENERGY\x10\n\x12\x0f\n\x0bOUT_OF_TIME\x10\x0b\x12\x17\n\x13JVM_STACK_OVER_FLOW\x10\x0c\x12\x0b\n\x07UNKNOWN\x10\r\x12\x13\n\x0fTRANSFER_FAILED\x10\x0e\x1a\x83\x02\n\x03raw\x12\x17\n\x0fref_block_bytes\x18\x01 \x01(\x0c\x12\x15\n\rref_block_num\x18\x03 \x01(\x03\x12\x16\n\x0eref_block_hash\x18\x04 \x01(\x0c\x12\x12\n\nexpiration\x18\x08 \x01(\x03\x12\"\n\x05\x61uths\x18\t \x03(\x0b\x32\x13.protocol.authority\x12\x13\n\x0b\x63ustom_data\x18\n \x01(\x0c\x12\x30\n\x08\x63ontract\x18\x0b \x03(\x0b\x32\x1e.protocol.Transaction.Contract\x12\x0f\n\x07scripts\x18\x0c \x01(\x0c\x12\x11\n\ttimestamp\x18\x0e \x01(\x03\x12\x11\n\tfee_limit\x18\x12 \x01(\x03\"&\n\x03Key\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06weight\x18\x02 \x01(\x03\"\xf1\x01\n\nPermission\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.protocol.Permission.PermissionType\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x17\n\x0fpermission_name\x18\x03 \x01(\t\x12\x11\n\tthreshold\x18\x04 \x01(\x03\x12\x11\n\tparent_id\x18\x05 \x01(\x05\x12\x12\n\noperations\x18\x06 \x01(\x0c\x12\x1b\n\x04keys\x18\x07 \x03(\x0b\x32\r.protocol.Key\"4\n\x0ePermissionType\x12\t\n\x05Owner\x10\x00\x12\x0b\n\x07Witness\x10\x01\x12\n\n\x06\x41\x63tive\x10\x02*7\n\x0b\x41\x63\x63ountType\x12\n\n\x06Normal\x10\x00\x12\x0e\n\nAssetIssue\x10\x01\x12\x0c\n\x08\x43ontract\x10\x02\x62\x06proto3')

_ACCOUNTTYPE = DESCRIPTOR.enum_types_by_name['AccountType']
AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
Normal = 0
AssetIssue = 1
Contract = 2


_EXCHANGE = DESCRIPTOR.message_types_by_name['Exchange']
_ACCOUNTID = DESCRIPTOR.message_types_by_name['AccountId']
_AUTHORITY = DESCRIPTOR.message_types_by_name['authority']
_TRANSACTION = DESCRIPTOR.message_types_by_name['Transaction']
_TRANSACTION_CONTRACT = _TRANSACTION.nested_types_by_name['Contract']
_TRANSACTION_RESULT = _TRANSACTION.nested_types_by_name['Result']
_TRANSACTION_RAW = _TRANSACTION.nested_types_by_name['raw']
_KEY = DESCRIPTOR.message_types_by_name['Key']
_PERMISSION = DESCRIPTOR.message_types_by_name['Permission']
_TRANSACTION_CONTRACT_CONTRACTTYPE = _TRANSACTION_CONTRACT.enum_types_by_name['ContractType']
_TRANSACTION_RESULT_CODE = _TRANSACTION_RESULT.enum_types_by_name['code']
_TRANSACTION_RESULT_CONTRACTRESULT = _TRANSACTION_RESULT.enum_types_by_name['contractResult']
_PERMISSION_PERMISSIONTYPE = _PERMISSION.enum_types_by_name['PermissionType']
Exchange = _reflection.GeneratedProtocolMessageType('Exchange', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGE,
  '__module__' : 'core.Tron_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Exchange)
  })
_sym_db.RegisterMessage(Exchange)

AccountId = _reflection.GeneratedProtocolMessageType('AccountId', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTID,
  '__module__' : 'core.Tron_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AccountId)
  })
_sym_db.RegisterMessage(AccountId)

authority = _reflection.GeneratedProtocolMessageType('authority', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORITY,
  '__module__' : 'core.Tron_pb2'
  # @@protoc_insertion_point(class_scope:protocol.authority)
  })
_sym_db.RegisterMessage(authority)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {

  'Contract' : _reflection.GeneratedProtocolMessageType('Contract', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTION_CONTRACT,
    '__module__' : 'core.Tron_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Transaction.Contract)
    })
  ,

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTION_RESULT,
    '__module__' : 'core.Tron_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Transaction.Result)
    })
  ,

  'raw' : _reflection.GeneratedProtocolMessageType('raw', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTION_RAW,
    '__module__' : 'core.Tron_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Transaction.raw)
    })
  ,
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'core.Tron_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Transaction)
  })
_sym_db.RegisterMessage(Transaction)
_sym_db.RegisterMessage(Transaction.Contract)
_sym_db.RegisterMessage(Transaction.Result)
_sym_db.RegisterMessage(Transaction.raw)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'core.Tron_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Key)
  })
_sym_db.RegisterMessage(Key)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'core.Tron_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Permission)
  })
_sym_db.RegisterMessage(Permission)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACCOUNTTYPE._serialized_start=2936
  _ACCOUNTTYPE._serialized_end=2991
  _EXCHANGE._serialized_start=57
  _EXCHANGE._serialized_end=242
  _ACCOUNTID._serialized_start=244
  _ACCOUNTID._serialized_end=286
  _AUTHORITY._serialized_start=288
  _AUTHORITY._serialized_end=362
  _TRANSACTION._serialized_start=365
  _TRANSACTION._serialized_end=2650
  _TRANSACTION_CONTRACT._serialized_start=488
  _TRANSACTION_CONTRACT._serialized_end=1701
  _TRANSACTION_CONTRACT_CONTRACTTYPE._serialized_start=664
  _TRANSACTION_CONTRACT_CONTRACTTYPE._serialized_end=1701
  _TRANSACTION_RESULT._serialized_start=1704
  _TRANSACTION_RESULT._serialized_end=2388
  _TRANSACTION_RESULT_CODE._serialized_start=2050
  _TRANSACTION_RESULT_CODE._serialized_end=2080
  _TRANSACTION_RESULT_CONTRACTRESULT._serialized_start=2083
  _TRANSACTION_RESULT_CONTRACTRESULT._serialized_end=2388
  _TRANSACTION_RAW._serialized_start=2391
  _TRANSACTION_RAW._serialized_end=2650
  _KEY._serialized_start=2652
  _KEY._serialized_end=2690
  _PERMISSION._serialized_start=2693
  _PERMISSION._serialized_end=2934
  _PERMISSION_PERMISSIONTYPE._serialized_start=2882
  _PERMISSION_PERMISSIONTYPE._serialized_end=2934
# @@protoc_insertion_point(module_scope)
