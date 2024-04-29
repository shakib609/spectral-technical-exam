from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MeterUsageRequest(_message.Message):
    __slots__ = ("page_number", "page_size")
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page_number: int
    page_size: int
    def __init__(self, page_number: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class MeterUsageResponse(_message.Message):
    __slots__ = ("data", "page_number", "page_size", "total_pages")
    DATA_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[MeterUsageData]
    page_number: int
    page_size: int
    total_pages: int
    def __init__(self, data: _Optional[_Iterable[_Union[MeterUsageData, _Mapping]]] = ..., page_number: _Optional[int] = ..., page_size: _Optional[int] = ..., total_pages: _Optional[int] = ...) -> None: ...

class MeterUsageData(_message.Message):
    __slots__ = ("time", "meterusage")
    TIME_FIELD_NUMBER: _ClassVar[int]
    METERUSAGE_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    meterusage: float
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., meterusage: _Optional[float] = ...) -> None: ...
