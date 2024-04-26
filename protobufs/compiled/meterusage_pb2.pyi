from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MeterUsageRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MeterUsageResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[MeterUsageData]
    def __init__(self, data: _Optional[_Iterable[_Union[MeterUsageData, _Mapping]]] = ...) -> None: ...

class MeterUsageData(_message.Message):
    __slots__ = ("time", "meterusage")
    TIME_FIELD_NUMBER: _ClassVar[int]
    METERUSAGE_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    meterusage: float
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., meterusage: _Optional[float] = ...) -> None: ...
