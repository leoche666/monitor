# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msgid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msgid.proto',
  package='tbsproto',
  serialized_pb=_b('\n\x0bmsgid.proto\x12\x08tbsproto*@\n\tEnumMsgID\x12\x0f\n\x0bMsg_Request\x10\x01\x12\x10\n\x0cMsg_Response\x10\x02\x12\x10\n\x0cMsg_PushData\x10\x03\x42\x38\n\x1e\x63om.thebeastshop.monitor.protoB\x16TheBeastShopMsgIDProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ENUMMSGID = _descriptor.EnumDescriptor(
  name='EnumMsgID',
  full_name='tbsproto.EnumMsgID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Msg_Request', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Msg_Response', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Msg_PushData', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=25,
  serialized_end=89,
)
_sym_db.RegisterEnumDescriptor(_ENUMMSGID)

EnumMsgID = enum_type_wrapper.EnumTypeWrapper(_ENUMMSGID)
Msg_Request = 1
Msg_Response = 2
Msg_PushData = 3


DESCRIPTOR.enum_types_by_name['EnumMsgID'] = _ENUMMSGID


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.thebeastshop.monitor.protoB\026TheBeastShopMsgIDProto'))
# @@protoc_insertion_point(module_scope)
