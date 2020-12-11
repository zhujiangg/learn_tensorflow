# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communicator_objects/engine_configuration_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='communicator_objects/engine_configuration_proto.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n5communicator_objects/engine_configuration_proto.proto\x12\x14\x63ommunicator_objects\"\x95\x01 numpy\n\x18\x45ngineConfigurationProto\x12\r\n\x05width\x18\x01 numpy \x01 numpy(\x05\x12\x0e\n\x06height\x18\x02 \x01 numpy(\x05\x12\x15\n\rquality_level\x18\x03 \x01 numpy(\x05\x12\x12\n\ntime_scale\x18\x04 \x01 numpy(\x02\x12\x19\n\x11target_frame_rate\x18\x05 \x01 numpy(\x05\x12\x14\n\x0cshow_monitor\x18\x06 \x01 numpy(\x08\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
)




_ENGINECONFIGURATIONPROTO = _descriptor.Descriptor(
  name='EngineConfigurationProto',
  full_name='communicator_objects.EngineConfigurationProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='communicator_objects.EngineConfigurationProto.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='communicator_objects.EngineConfigurationProto.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quality_level', full_name='communicator_objects.EngineConfigurationProto.quality_level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_scale', full_name='communicator_objects.EngineConfigurationProto.time_scale', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_frame_rate', full_name='communicator_objects.EngineConfigurationProto.target_frame_rate', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_monitor', full_name='communicator_objects.EngineConfigurationProto.show_monitor', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=229,
)

DESCRIPTOR.message_types_by_name['EngineConfigurationProto'] = _ENGINECONFIGURATIONPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EngineConfigurationProto = _reflection.GeneratedProtocolMessageType('EngineConfigurationProto', (_message.Message,), dict(
  DESCRIPTOR = _ENGINECONFIGURATIONPROTO,
  __module__ = 'communicator_objects.engine_configuration_proto_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.EngineConfigurationProto)
  ))
_sym_db.RegisterMessage(EngineConfigurationProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\034MLAgents.CommunicatorObjects'))
# @@protoc_insertion_point(module_scope)
