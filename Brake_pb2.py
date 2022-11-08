# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Brake.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import SensorStates_pb2 as SensorStates__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Brake.proto',
  package='pb.SensorNearData',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0b\x42rake.proto\x12\x11pb.SensorNearData\x1a\x0cheader.proto\x1a\x12SensorStates.proto\"\xcf\x02\n\x05\x42rake\x12\x1a\n\x06header\x18\x01 \x01(\x0b\x32\n.pb.Header\x12+\n\x04\x65rrs\x18\x03 \x01(\x0b\x32\x1d.pb.SensorNearData.Brake.Errs\x12\x31\n\x07signals\x18\x04 \x01(\x0b\x32 .pb.SensorNearData.Brake.Signals\x12\x36\n\ntimestamps\x18\x06 \x01(\x0b\x32\".pb.SensorNearData.Brake.Timestamp\x1a?\n\x04\x45rrs\x12\x37\n\x10is_brake_applied\x18\x02 \x01(\x0e\x32\x10.pb.SensorStates:\x0bSTATE_FAULT\x1a*\n\x07Signals\x12\x1f\n\x10is_brake_applied\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a%\n\tTimestamp\x12\x18\n\x10is_brake_applied\x18\x02 \x01(\x12'
  ,
  dependencies=[header__pb2.DESCRIPTOR,SensorStates__pb2.DESCRIPTOR,])




_BRAKE_ERRS = _descriptor.Descriptor(
  name='Errs',
  full_name='pb.SensorNearData.Brake.Errs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_brake_applied', full_name='pb.SensorNearData.Brake.Errs.is_brake_applied', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=321,
)

_BRAKE_SIGNALS = _descriptor.Descriptor(
  name='Signals',
  full_name='pb.SensorNearData.Brake.Signals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_brake_applied', full_name='pb.SensorNearData.Brake.Signals.is_brake_applied', index=0,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=365,
)

_BRAKE_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='pb.SensorNearData.Brake.Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_brake_applied', full_name='pb.SensorNearData.Brake.Timestamp.is_brake_applied', index=0,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=404,
)

_BRAKE = _descriptor.Descriptor(
  name='Brake',
  full_name='pb.SensorNearData.Brake',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='pb.SensorNearData.Brake.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errs', full_name='pb.SensorNearData.Brake.errs', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signals', full_name='pb.SensorNearData.Brake.signals', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamps', full_name='pb.SensorNearData.Brake.timestamps', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BRAKE_ERRS, _BRAKE_SIGNALS, _BRAKE_TIMESTAMP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=404,
)

_BRAKE_ERRS.fields_by_name['is_brake_applied'].enum_type = SensorStates__pb2._SENSORSTATES
_BRAKE_ERRS.containing_type = _BRAKE
_BRAKE_SIGNALS.containing_type = _BRAKE
_BRAKE_TIMESTAMP.containing_type = _BRAKE
_BRAKE.fields_by_name['header'].message_type = header__pb2._HEADER
_BRAKE.fields_by_name['errs'].message_type = _BRAKE_ERRS
_BRAKE.fields_by_name['signals'].message_type = _BRAKE_SIGNALS
_BRAKE.fields_by_name['timestamps'].message_type = _BRAKE_TIMESTAMP
DESCRIPTOR.message_types_by_name['Brake'] = _BRAKE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Brake = _reflection.GeneratedProtocolMessageType('Brake', (_message.Message,), {

  'Errs' : _reflection.GeneratedProtocolMessageType('Errs', (_message.Message,), {
    'DESCRIPTOR' : _BRAKE_ERRS,
    '__module__' : 'Brake_pb2'
    # @@protoc_insertion_point(class_scope:pb.SensorNearData.Brake.Errs)
    })
  ,

  'Signals' : _reflection.GeneratedProtocolMessageType('Signals', (_message.Message,), {
    'DESCRIPTOR' : _BRAKE_SIGNALS,
    '__module__' : 'Brake_pb2'
    # @@protoc_insertion_point(class_scope:pb.SensorNearData.Brake.Signals)
    })
  ,

  'Timestamp' : _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
    'DESCRIPTOR' : _BRAKE_TIMESTAMP,
    '__module__' : 'Brake_pb2'
    # @@protoc_insertion_point(class_scope:pb.SensorNearData.Brake.Timestamp)
    })
  ,
  'DESCRIPTOR' : _BRAKE,
  '__module__' : 'Brake_pb2'
  # @@protoc_insertion_point(class_scope:pb.SensorNearData.Brake)
  })
_sym_db.RegisterMessage(Brake)
_sym_db.RegisterMessage(Brake.Errs)
_sym_db.RegisterMessage(Brake.Signals)
_sym_db.RegisterMessage(Brake.Timestamp)


# @@protoc_insertion_point(module_scope)
