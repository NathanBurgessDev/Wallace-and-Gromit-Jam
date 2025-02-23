from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MoveTo(_message.Message):
    __slots__ = ("azimuth", "altitude", "accelRate", "speedRate")
    AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    ACCELRATE_FIELD_NUMBER: _ClassVar[int]
    SPEEDRATE_FIELD_NUMBER: _ClassVar[int]
    azimuth: int
    altitude: int
    accelRate: int
    speedRate: int
    def __init__(self, azimuth: _Optional[int] = ..., altitude: _Optional[int] = ..., accelRate: _Optional[int] = ..., speedRate: _Optional[int] = ...) -> None: ...
