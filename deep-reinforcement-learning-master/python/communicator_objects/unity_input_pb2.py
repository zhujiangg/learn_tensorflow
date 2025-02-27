# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communicator_objects/unity_input.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from communicator_objects import unity_rl_input_pb2 as communicator__objects_dot_unity__rl__input__pb2
from communicator_objects import unity_rl_initialization_input_pb2 as communicator__objects_dot_unity__rl__initialization__input__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='communicator_objects/unity_input.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n&communicator_objects/unity_input.proto\x12\x14\x63ommunicator_objects\x1a)communicator_objects/unity_rl_input.proto\x1a\x38\x63ommunicator_objects/unity_rl_initialization_input.proto\"\xb0\x01 numpy\n\nUnityInput\x12\x34\n\x08rl_input\x18\x01 numpy \x01 numpy(\x0b\x32\".communicator_objects.UnityRLInput\x12Q\n\x17rl_initialization_input\x18\x02 \x01 numpy(\x0b\x32\x30.communicator_objects.UnityRLInitializationInput\x12\x19\n\x11\x63ustom_data_input\x18\x03 \x01 numpy(\x05\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[communicator__objects_dot_unity__rl__input__pb2.DESCRIPTOR,communicator__objects_dot_unity__rl__initialization__input__pb2.DESCRIPTOR,])




_UNITYINPUT = _descriptor.Descriptor(
  name='UnityInput',
  full_name='communicator_objects.UnityInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rl_input', full_name='communicator_objects.UnityInput.rl_input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rl_initialization_input', full_name='communicator_objects.UnityInput.rl_initialization_input', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_data_input', full_name='communicator_objects.UnityInput.custom_data_input', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=166,
  serialized_end=342,
)

_UNITYINPUT.fields_by_name['rl_input'].message_type = communicator__objects_dot_unity__rl__input__pb2._UNITYRLINPUT
_UNITYINPUT.fields_by_name['rl_initialization_input'].message_type = communicator__objects_dot_unity__rl__initialization__input__pb2._UNITYRLINITIALIZATIONINPUT
DESCRIPTOR.message_types_by_name['UnityInput'] = _UNITYINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityInput = _reflection.GeneratedProtocolMessageType('UnityInput', (_message.Message,), dict(
  DESCRIPTOR = _UNITYINPUT,
  __module__ = 'communicator_objects.unity_input_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityInput)
  ))
_sym_db.RegisterMessage(UnityInput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\034MLAgents.CommunicatorObjects'))
# @@protoc_insertion_point(module_scope)
