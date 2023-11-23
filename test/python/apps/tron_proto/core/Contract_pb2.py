# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/Contract.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from core import Tron_pb2 as core_dot_Tron__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ore/Contract.proto\x12\x08protocol\x1a\x0f\x63ore/Tron.proto\"l\n\x15\x41\x63\x63ountCreateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61\x63\x63ount_address\x18\x02 \x01(\x0c\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.protocol.AccountType\"D\n\x15\x41\x63\x63ountUpdateContract\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\x0c\x12\x15\n\rowner_address\x18\x02 \x01(\x0c\"M\n\x10TransferContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x12\n\nto_address\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"f\n\x15TransferAssetContract\x12\x12\n\nasset_name\x18\x01 \x01(\x0c\x12\x15\n\rowner_address\x18\x02 \x01(\x0c\x12\x12\n\nto_address\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\"`\n\x11VoteAssetContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x14\n\x0cvote_address\x18\x02 \x03(\x0c\x12\x0f\n\x07support\x18\x03 \x01(\x08\x12\r\n\x05\x63ount\x18\x05 \x01(\x05\"\xa2\x01\n\x13VoteWitnessContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x31\n\x05votes\x18\x02 \x03(\x0b\x32\".protocol.VoteWitnessContract.Vote\x12\x0f\n\x07support\x18\x03 \x01(\x08\x1a\x30\n\x04Vote\x12\x14\n\x0cvote_address\x18\x01 \x01(\x0c\x12\x12\n\nvote_count\x18\x02 \x01(\x03\";\n\x15WitnessCreateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x0b\n\x03url\x18\x02 \x01(\x0c\"B\n\x15WitnessUpdateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x12\n\nupdate_url\x18\x0c \x01(\x0c\"\xe2\x03\n\x12\x41ssetIssueContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\x0c\x12\x0c\n\x04\x61\x62\x62r\x18\x03 \x01(\x0c\x12\x14\n\x0ctotal_supply\x18\x04 \x01(\x03\x12@\n\rfrozen_supply\x18\x05 \x03(\x0b\x32).protocol.AssetIssueContract.FrozenSupply\x12\x0f\n\x07trx_num\x18\x06 \x01(\x05\x12\x0b\n\x03num\x18\x08 \x01(\x05\x12\x12\n\nstart_time\x18\t \x01(\x03\x12\x10\n\x08\x65nd_time\x18\n \x01(\x03\x12\x12\n\nvote_score\x18\x10 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x14 \x01(\x0c\x12\x0b\n\x03url\x18\x15 \x01(\x0c\x12\x1c\n\x14\x66ree_asset_net_limit\x18\x16 \x01(\x03\x12#\n\x1bpublic_free_asset_net_limit\x18\x17 \x01(\x03\x12#\n\x1bpublic_free_asset_net_usage\x18\x18 \x01(\x03\x12#\n\x1bpublic_latest_free_net_time\x18\x19 \x01(\x03\x1a:\n\x0c\x46rozenSupply\x12\x15\n\rfrozen_amount\x18\x01 \x01(\x03\x12\x13\n\x0b\x66rozen_days\x18\x02 \x01(\x03\"n\n\x1dParticipateAssetIssueContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x12\n\nto_address\x18\x02 \x01(\x0c\x12\x12\n\nasset_name\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\"7\n\x0e\x44\x65ployContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x0e\n\x06script\x18\x02 \x01(\x0c\"\xa3\x01\n\x15\x46reezeBalanceContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x16\n\x0e\x66rozen_balance\x18\x02 \x01(\x03\x12\x17\n\x0f\x66rozen_duration\x18\x03 \x01(\x03\x12(\n\x08resource\x18\n \x01(\x0e\x32\x16.protocol.ResourceCode\x12\x18\n\x10receiver_address\x18\x0f \x01(\x0c\"t\n\x17UnfreezeBalanceContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12(\n\x08resource\x18\n \x01(\x0e\x32\x16.protocol.ResourceCode\x12\x18\n\x10receiver_address\x18\x0f \x01(\x0c\"r\n\x17\x46reezeBalanceV2Contract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x16\n\x0e\x66rozen_balance\x18\x02 \x01(\x03\x12(\n\x08resource\x18\x03 \x01(\x0e\x32\x16.protocol.ResourceCode\"v\n\x19UnfreezeBalanceV2Contract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x18\n\x10unfreeze_balance\x18\x02 \x01(\x03\x12(\n\x08resource\x18\x03 \x01(\x0e\x32\x16.protocol.ResourceCode\"7\n\x1eWithdrawExpireUnfreezeContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\"\x94\x01\n\x18\x44\x65legateResourceContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12(\n\x08resource\x18\x02 \x01(\x0e\x32\x16.protocol.ResourceCode\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x03\x12\x18\n\x10receiver_address\x18\x04 \x01(\x0c\x12\x0c\n\x04lock\x18\x05 \x01(\x08\"\x88\x01\n\x1aUnDelegateResourceContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12(\n\x08resource\x18\x02 \x01(\x0e\x32\x16.protocol.ResourceCode\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x03\x12\x18\n\x10receiver_address\x18\x04 \x01(\x0c\".\n\x15UnfreezeAssetContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\"0\n\x17WithdrawBalanceContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\"{\n\x13UpdateAssetContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\x0c\x12\x0b\n\x03url\x18\x03 \x01(\x0c\x12\x11\n\tnew_limit\x18\x04 \x01(\x03\x12\x18\n\x10new_public_limit\x18\x05 \x01(\x03\"\xa8\x01\n\x16ProposalCreateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x44\n\nparameters\x18\x02 \x03(\x0b\x32\x30.protocol.ProposalCreateContract.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"^\n\x17ProposalApproveContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x03\x12\x17\n\x0fis_add_approval\x18\x03 \x01(\x08\"D\n\x16ProposalDeleteContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x03\"\x95\x01\n\x14TriggerSmartContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\x0c\x12\x12\n\ncall_value\x18\x03 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x18\n\x10\x63\x61ll_token_value\x18\x05 \x01(\x03\x12\x10\n\x08token_id\x18\x06 \x01(\x03\"\x9b\x01\n\x16\x45xchangeCreateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x16\n\x0e\x66irst_token_id\x18\x02 \x01(\x0c\x12\x1b\n\x13\x66irst_token_balance\x18\x03 \x01(\x03\x12\x17\n\x0fsecond_token_id\x18\x04 \x01(\x0c\x12\x1c\n\x14second_token_balance\x18\x05 \x01(\x03\"e\n\x16\x45xchangeInjectContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\x03\x12\x10\n\x08token_id\x18\x03 \x01(\x0c\x12\r\n\x05quant\x18\x04 \x01(\x03\"g\n\x18\x45xchangeWithdrawContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\x03\x12\x10\n\x08token_id\x18\x03 \x01(\x0c\x12\r\n\x05quant\x18\x04 \x01(\x03\"|\n\x1b\x45xchangeTransactionContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\x03\x12\x10\n\x08token_id\x18\x03 \x01(\x0c\x12\r\n\x05quant\x18\x04 \x01(\x03\x12\x10\n\x08\x65xpected\x18\x05 \x01(\x03\"\xab\x01\n\x1f\x41\x63\x63ountPermissionUpdateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12#\n\x05owner\x18\x02 \x01(\x0b\x32\x14.protocol.Permission\x12%\n\x07witness\x18\x03 \x01(\x0b\x32\x14.protocol.Permission\x12%\n\x07\x61\x63tives\x18\x04 \x03(\x0b\x32\x14.protocol.Permission*)\n\x0cResourceCode\x12\r\n\tBANDWIDTH\x10\x00\x12\n\n\x06\x45NERGY\x10\x01\x42\x46\n\x0forg.tron.protosB\x08\x43ontractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')

_RESOURCECODE = DESCRIPTOR.enum_types_by_name['ResourceCode']
ResourceCode = enum_type_wrapper.EnumTypeWrapper(_RESOURCECODE)
BANDWIDTH = 0
ENERGY = 1


_ACCOUNTCREATECONTRACT = DESCRIPTOR.message_types_by_name['AccountCreateContract']
_ACCOUNTUPDATECONTRACT = DESCRIPTOR.message_types_by_name['AccountUpdateContract']
_TRANSFERCONTRACT = DESCRIPTOR.message_types_by_name['TransferContract']
_TRANSFERASSETCONTRACT = DESCRIPTOR.message_types_by_name['TransferAssetContract']
_VOTEASSETCONTRACT = DESCRIPTOR.message_types_by_name['VoteAssetContract']
_VOTEWITNESSCONTRACT = DESCRIPTOR.message_types_by_name['VoteWitnessContract']
_VOTEWITNESSCONTRACT_VOTE = _VOTEWITNESSCONTRACT.nested_types_by_name['Vote']
_WITNESSCREATECONTRACT = DESCRIPTOR.message_types_by_name['WitnessCreateContract']
_WITNESSUPDATECONTRACT = DESCRIPTOR.message_types_by_name['WitnessUpdateContract']
_ASSETISSUECONTRACT = DESCRIPTOR.message_types_by_name['AssetIssueContract']
_ASSETISSUECONTRACT_FROZENSUPPLY = _ASSETISSUECONTRACT.nested_types_by_name['FrozenSupply']
_PARTICIPATEASSETISSUECONTRACT = DESCRIPTOR.message_types_by_name['ParticipateAssetIssueContract']
_DEPLOYCONTRACT = DESCRIPTOR.message_types_by_name['DeployContract']
_FREEZEBALANCECONTRACT = DESCRIPTOR.message_types_by_name['FreezeBalanceContract']
_UNFREEZEBALANCECONTRACT = DESCRIPTOR.message_types_by_name['UnfreezeBalanceContract']
_FREEZEBALANCEV2CONTRACT = DESCRIPTOR.message_types_by_name['FreezeBalanceV2Contract']
_UNFREEZEBALANCEV2CONTRACT = DESCRIPTOR.message_types_by_name['UnfreezeBalanceV2Contract']
_WITHDRAWEXPIREUNFREEZECONTRACT = DESCRIPTOR.message_types_by_name['WithdrawExpireUnfreezeContract']
_DELEGATERESOURCECONTRACT = DESCRIPTOR.message_types_by_name['DelegateResourceContract']
_UNDELEGATERESOURCECONTRACT = DESCRIPTOR.message_types_by_name['UnDelegateResourceContract']
_UNFREEZEASSETCONTRACT = DESCRIPTOR.message_types_by_name['UnfreezeAssetContract']
_WITHDRAWBALANCECONTRACT = DESCRIPTOR.message_types_by_name['WithdrawBalanceContract']
_UPDATEASSETCONTRACT = DESCRIPTOR.message_types_by_name['UpdateAssetContract']
_PROPOSALCREATECONTRACT = DESCRIPTOR.message_types_by_name['ProposalCreateContract']
_PROPOSALCREATECONTRACT_PARAMETERSENTRY = _PROPOSALCREATECONTRACT.nested_types_by_name['ParametersEntry']
_PROPOSALAPPROVECONTRACT = DESCRIPTOR.message_types_by_name['ProposalApproveContract']
_PROPOSALDELETECONTRACT = DESCRIPTOR.message_types_by_name['ProposalDeleteContract']
_TRIGGERSMARTCONTRACT = DESCRIPTOR.message_types_by_name['TriggerSmartContract']
_EXCHANGECREATECONTRACT = DESCRIPTOR.message_types_by_name['ExchangeCreateContract']
_EXCHANGEINJECTCONTRACT = DESCRIPTOR.message_types_by_name['ExchangeInjectContract']
_EXCHANGEWITHDRAWCONTRACT = DESCRIPTOR.message_types_by_name['ExchangeWithdrawContract']
_EXCHANGETRANSACTIONCONTRACT = DESCRIPTOR.message_types_by_name['ExchangeTransactionContract']
_ACCOUNTPERMISSIONUPDATECONTRACT = DESCRIPTOR.message_types_by_name['AccountPermissionUpdateContract']
AccountCreateContract = _reflection.GeneratedProtocolMessageType('AccountCreateContract', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTCREATECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AccountCreateContract)
  })
_sym_db.RegisterMessage(AccountCreateContract)

AccountUpdateContract = _reflection.GeneratedProtocolMessageType('AccountUpdateContract', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTUPDATECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AccountUpdateContract)
  })
_sym_db.RegisterMessage(AccountUpdateContract)

TransferContract = _reflection.GeneratedProtocolMessageType('TransferContract', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.TransferContract)
  })
_sym_db.RegisterMessage(TransferContract)

TransferAssetContract = _reflection.GeneratedProtocolMessageType('TransferAssetContract', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERASSETCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.TransferAssetContract)
  })
_sym_db.RegisterMessage(TransferAssetContract)

VoteAssetContract = _reflection.GeneratedProtocolMessageType('VoteAssetContract', (_message.Message,), {
  'DESCRIPTOR' : _VOTEASSETCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.VoteAssetContract)
  })
_sym_db.RegisterMessage(VoteAssetContract)

VoteWitnessContract = _reflection.GeneratedProtocolMessageType('VoteWitnessContract', (_message.Message,), {

  'Vote' : _reflection.GeneratedProtocolMessageType('Vote', (_message.Message,), {
    'DESCRIPTOR' : _VOTEWITNESSCONTRACT_VOTE,
    '__module__' : 'core.Contract_pb2'
    # @@protoc_insertion_point(class_scope:protocol.VoteWitnessContract.Vote)
    })
  ,
  'DESCRIPTOR' : _VOTEWITNESSCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.VoteWitnessContract)
  })
_sym_db.RegisterMessage(VoteWitnessContract)
_sym_db.RegisterMessage(VoteWitnessContract.Vote)

WitnessCreateContract = _reflection.GeneratedProtocolMessageType('WitnessCreateContract', (_message.Message,), {
  'DESCRIPTOR' : _WITNESSCREATECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.WitnessCreateContract)
  })
_sym_db.RegisterMessage(WitnessCreateContract)

WitnessUpdateContract = _reflection.GeneratedProtocolMessageType('WitnessUpdateContract', (_message.Message,), {
  'DESCRIPTOR' : _WITNESSUPDATECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.WitnessUpdateContract)
  })
_sym_db.RegisterMessage(WitnessUpdateContract)

AssetIssueContract = _reflection.GeneratedProtocolMessageType('AssetIssueContract', (_message.Message,), {

  'FrozenSupply' : _reflection.GeneratedProtocolMessageType('FrozenSupply', (_message.Message,), {
    'DESCRIPTOR' : _ASSETISSUECONTRACT_FROZENSUPPLY,
    '__module__' : 'core.Contract_pb2'
    # @@protoc_insertion_point(class_scope:protocol.AssetIssueContract.FrozenSupply)
    })
  ,
  'DESCRIPTOR' : _ASSETISSUECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AssetIssueContract)
  })
_sym_db.RegisterMessage(AssetIssueContract)
_sym_db.RegisterMessage(AssetIssueContract.FrozenSupply)

ParticipateAssetIssueContract = _reflection.GeneratedProtocolMessageType('ParticipateAssetIssueContract', (_message.Message,), {
  'DESCRIPTOR' : _PARTICIPATEASSETISSUECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ParticipateAssetIssueContract)
  })
_sym_db.RegisterMessage(ParticipateAssetIssueContract)

DeployContract = _reflection.GeneratedProtocolMessageType('DeployContract', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.DeployContract)
  })
_sym_db.RegisterMessage(DeployContract)

FreezeBalanceContract = _reflection.GeneratedProtocolMessageType('FreezeBalanceContract', (_message.Message,), {
  'DESCRIPTOR' : _FREEZEBALANCECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.FreezeBalanceContract)
  })
_sym_db.RegisterMessage(FreezeBalanceContract)

UnfreezeBalanceContract = _reflection.GeneratedProtocolMessageType('UnfreezeBalanceContract', (_message.Message,), {
  'DESCRIPTOR' : _UNFREEZEBALANCECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.UnfreezeBalanceContract)
  })
_sym_db.RegisterMessage(UnfreezeBalanceContract)

FreezeBalanceV2Contract = _reflection.GeneratedProtocolMessageType('FreezeBalanceV2Contract', (_message.Message,), {
  'DESCRIPTOR' : _FREEZEBALANCEV2CONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.FreezeBalanceV2Contract)
  })
_sym_db.RegisterMessage(FreezeBalanceV2Contract)

UnfreezeBalanceV2Contract = _reflection.GeneratedProtocolMessageType('UnfreezeBalanceV2Contract', (_message.Message,), {
  'DESCRIPTOR' : _UNFREEZEBALANCEV2CONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.UnfreezeBalanceV2Contract)
  })
_sym_db.RegisterMessage(UnfreezeBalanceV2Contract)

WithdrawExpireUnfreezeContract = _reflection.GeneratedProtocolMessageType('WithdrawExpireUnfreezeContract', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWEXPIREUNFREEZECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.WithdrawExpireUnfreezeContract)
  })
_sym_db.RegisterMessage(WithdrawExpireUnfreezeContract)

DelegateResourceContract = _reflection.GeneratedProtocolMessageType('DelegateResourceContract', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATERESOURCECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.DelegateResourceContract)
  })
_sym_db.RegisterMessage(DelegateResourceContract)

UnDelegateResourceContract = _reflection.GeneratedProtocolMessageType('UnDelegateResourceContract', (_message.Message,), {
  'DESCRIPTOR' : _UNDELEGATERESOURCECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.UnDelegateResourceContract)
  })
_sym_db.RegisterMessage(UnDelegateResourceContract)

UnfreezeAssetContract = _reflection.GeneratedProtocolMessageType('UnfreezeAssetContract', (_message.Message,), {
  'DESCRIPTOR' : _UNFREEZEASSETCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.UnfreezeAssetContract)
  })
_sym_db.RegisterMessage(UnfreezeAssetContract)

WithdrawBalanceContract = _reflection.GeneratedProtocolMessageType('WithdrawBalanceContract', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWBALANCECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.WithdrawBalanceContract)
  })
_sym_db.RegisterMessage(WithdrawBalanceContract)

UpdateAssetContract = _reflection.GeneratedProtocolMessageType('UpdateAssetContract', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEASSETCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.UpdateAssetContract)
  })
_sym_db.RegisterMessage(UpdateAssetContract)

ProposalCreateContract = _reflection.GeneratedProtocolMessageType('ProposalCreateContract', (_message.Message,), {

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROPOSALCREATECONTRACT_PARAMETERSENTRY,
    '__module__' : 'core.Contract_pb2'
    # @@protoc_insertion_point(class_scope:protocol.ProposalCreateContract.ParametersEntry)
    })
  ,
  'DESCRIPTOR' : _PROPOSALCREATECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ProposalCreateContract)
  })
_sym_db.RegisterMessage(ProposalCreateContract)
_sym_db.RegisterMessage(ProposalCreateContract.ParametersEntry)

ProposalApproveContract = _reflection.GeneratedProtocolMessageType('ProposalApproveContract', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSALAPPROVECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ProposalApproveContract)
  })
_sym_db.RegisterMessage(ProposalApproveContract)

ProposalDeleteContract = _reflection.GeneratedProtocolMessageType('ProposalDeleteContract', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSALDELETECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ProposalDeleteContract)
  })
_sym_db.RegisterMessage(ProposalDeleteContract)

TriggerSmartContract = _reflection.GeneratedProtocolMessageType('TriggerSmartContract', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERSMARTCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.TriggerSmartContract)
  })
_sym_db.RegisterMessage(TriggerSmartContract)

ExchangeCreateContract = _reflection.GeneratedProtocolMessageType('ExchangeCreateContract', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGECREATECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ExchangeCreateContract)
  })
_sym_db.RegisterMessage(ExchangeCreateContract)

ExchangeInjectContract = _reflection.GeneratedProtocolMessageType('ExchangeInjectContract', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGEINJECTCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ExchangeInjectContract)
  })
_sym_db.RegisterMessage(ExchangeInjectContract)

ExchangeWithdrawContract = _reflection.GeneratedProtocolMessageType('ExchangeWithdrawContract', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGEWITHDRAWCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ExchangeWithdrawContract)
  })
_sym_db.RegisterMessage(ExchangeWithdrawContract)

ExchangeTransactionContract = _reflection.GeneratedProtocolMessageType('ExchangeTransactionContract', (_message.Message,), {
  'DESCRIPTOR' : _EXCHANGETRANSACTIONCONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ExchangeTransactionContract)
  })
_sym_db.RegisterMessage(ExchangeTransactionContract)

AccountPermissionUpdateContract = _reflection.GeneratedProtocolMessageType('AccountPermissionUpdateContract', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTPERMISSIONUPDATECONTRACT,
  '__module__' : 'core.Contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.AccountPermissionUpdateContract)
  })
_sym_db.RegisterMessage(AccountPermissionUpdateContract)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017org.tron.protosB\010ContractZ)github.com/tronprotocol/grpc-gateway/core'
  _PROPOSALCREATECONTRACT_PARAMETERSENTRY._options = None
  _PROPOSALCREATECONTRACT_PARAMETERSENTRY._serialized_options = b'8\001'
  _RESOURCECODE._serialized_start=3704
  _RESOURCECODE._serialized_end=3745
  _ACCOUNTCREATECONTRACT._serialized_start=50
  _ACCOUNTCREATECONTRACT._serialized_end=158
  _ACCOUNTUPDATECONTRACT._serialized_start=160
  _ACCOUNTUPDATECONTRACT._serialized_end=228
  _TRANSFERCONTRACT._serialized_start=230
  _TRANSFERCONTRACT._serialized_end=307
  _TRANSFERASSETCONTRACT._serialized_start=309
  _TRANSFERASSETCONTRACT._serialized_end=411
  _VOTEASSETCONTRACT._serialized_start=413
  _VOTEASSETCONTRACT._serialized_end=509
  _VOTEWITNESSCONTRACT._serialized_start=512
  _VOTEWITNESSCONTRACT._serialized_end=674
  _VOTEWITNESSCONTRACT_VOTE._serialized_start=626
  _VOTEWITNESSCONTRACT_VOTE._serialized_end=674
  _WITNESSCREATECONTRACT._serialized_start=676
  _WITNESSCREATECONTRACT._serialized_end=735
  _WITNESSUPDATECONTRACT._serialized_start=737
  _WITNESSUPDATECONTRACT._serialized_end=803
  _ASSETISSUECONTRACT._serialized_start=806
  _ASSETISSUECONTRACT._serialized_end=1288
  _ASSETISSUECONTRACT_FROZENSUPPLY._serialized_start=1230
  _ASSETISSUECONTRACT_FROZENSUPPLY._serialized_end=1288
  _PARTICIPATEASSETISSUECONTRACT._serialized_start=1290
  _PARTICIPATEASSETISSUECONTRACT._serialized_end=1400
  _DEPLOYCONTRACT._serialized_start=1402
  _DEPLOYCONTRACT._serialized_end=1457
  _FREEZEBALANCECONTRACT._serialized_start=1460
  _FREEZEBALANCECONTRACT._serialized_end=1623
  _UNFREEZEBALANCECONTRACT._serialized_start=1625
  _UNFREEZEBALANCECONTRACT._serialized_end=1741
  _FREEZEBALANCEV2CONTRACT._serialized_start=1743
  _FREEZEBALANCEV2CONTRACT._serialized_end=1857
  _UNFREEZEBALANCEV2CONTRACT._serialized_start=1859
  _UNFREEZEBALANCEV2CONTRACT._serialized_end=1977
  _WITHDRAWEXPIREUNFREEZECONTRACT._serialized_start=1979
  _WITHDRAWEXPIREUNFREEZECONTRACT._serialized_end=2034
  _DELEGATERESOURCECONTRACT._serialized_start=2037
  _DELEGATERESOURCECONTRACT._serialized_end=2185
  _UNDELEGATERESOURCECONTRACT._serialized_start=2188
  _UNDELEGATERESOURCECONTRACT._serialized_end=2324
  _UNFREEZEASSETCONTRACT._serialized_start=2326
  _UNFREEZEASSETCONTRACT._serialized_end=2372
  _WITHDRAWBALANCECONTRACT._serialized_start=2374
  _WITHDRAWBALANCECONTRACT._serialized_end=2422
  _UPDATEASSETCONTRACT._serialized_start=2424
  _UPDATEASSETCONTRACT._serialized_end=2547
  _PROPOSALCREATECONTRACT._serialized_start=2550
  _PROPOSALCREATECONTRACT._serialized_end=2718
  _PROPOSALCREATECONTRACT_PARAMETERSENTRY._serialized_start=2669
  _PROPOSALCREATECONTRACT_PARAMETERSENTRY._serialized_end=2718
  _PROPOSALAPPROVECONTRACT._serialized_start=2720
  _PROPOSALAPPROVECONTRACT._serialized_end=2814
  _PROPOSALDELETECONTRACT._serialized_start=2816
  _PROPOSALDELETECONTRACT._serialized_end=2884
  _TRIGGERSMARTCONTRACT._serialized_start=2887
  _TRIGGERSMARTCONTRACT._serialized_end=3036
  _EXCHANGECREATECONTRACT._serialized_start=3039
  _EXCHANGECREATECONTRACT._serialized_end=3194
  _EXCHANGEINJECTCONTRACT._serialized_start=3196
  _EXCHANGEINJECTCONTRACT._serialized_end=3297
  _EXCHANGEWITHDRAWCONTRACT._serialized_start=3299
  _EXCHANGEWITHDRAWCONTRACT._serialized_end=3402
  _EXCHANGETRANSACTIONCONTRACT._serialized_start=3404
  _EXCHANGETRANSACTIONCONTRACT._serialized_end=3528
  _ACCOUNTPERMISSIONUPDATECONTRACT._serialized_start=3531
  _ACCOUNTPERMISSIONUPDATECONTRACT._serialized_end=3702
# @@protoc_insertion_point(module_scope)
