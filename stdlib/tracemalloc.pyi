import sys
from _tracemalloc import *
from typing import Any, Optional, Sequence, Union, overload
from typing_extensions import SupportsIndex

def get_object_traceback(obj: object) -> Traceback | None: ...
def take_snapshot() -> Snapshot: ...

class DomainFilter:
    inclusive: bool
    domain: int
    def __init__(self, inclusive: bool, domain: int) -> None: ...

class Filter:
    domain: int | None
    inclusive: bool
    lineno: int | None
    filename_pattern: str
    all_frames: bool
    def __init__(
        self, inclusive: bool, filename_pattern: str, lineno: int | None = ..., all_frames: bool = ..., domain: int | None = ...
    ) -> None: ...

class Statistic:
    count: int
    size: int
    traceback: Traceback
    def __init__(self, traceback: Traceback, size: int, count: int) -> None: ...

class StatisticDiff:
    count: int
    count_diff: int
    size: int
    size_diff: int
    traceback: Traceback
    def __init__(self, traceback: Traceback, size: int, size_diff: int, count: int, count_diff: int) -> None: ...

_FrameTupleT = tuple[str, int]

class Frame:
    filename: str
    lineno: int
    def __init__(self, frame: _FrameTupleT) -> None: ...
    def __lt__(self, other: Frame) -> bool: ...
    if sys.version_info >= (3, 11):
        def __gt__(self, other: Frame) -> bool: ...
        def __ge__(self, other: Frame) -> bool: ...
        def __le__(self, other: Frame) -> bool: ...
    else:
        def __gt__(self, other: Frame, NotImplemented: Any = ...) -> bool: ...
        def __ge__(self, other: Frame, NotImplemented: Any = ...) -> bool: ...
        def __le__(self, other: Frame, NotImplemented: Any = ...) -> bool: ...

if sys.version_info >= (3, 9):
    _TraceTupleT = Union[tuple[int, int, Sequence[_FrameTupleT], Optional[int]], tuple[int, int, Sequence[_FrameTupleT]]]
else:
    _TraceTupleT = tuple[int, int, Sequence[_FrameTupleT]]

class Trace:
    domain: int
    size: int
    traceback: Traceback
    def __init__(self, trace: _TraceTupleT) -> None: ...

class Traceback(Sequence[Frame]):
    if sys.version_info >= (3, 9):
        total_nframe: int | None
        def __init__(self, frames: Sequence[_FrameTupleT], total_nframe: int | None = ...) -> None: ...
    else:
        def __init__(self, frames: Sequence[_FrameTupleT]) -> None: ...
    if sys.version_info >= (3, 7):
        def format(self, limit: int | None = ..., most_recent_first: bool = ...) -> list[str]: ...
    else:
        def format(self, limit: int | None = ...) -> list[str]: ...

    @overload
    def __getitem__(self, i: SupportsIndex) -> Frame: ...
    @overload
    def __getitem__(self, s: slice) -> Sequence[Frame]: ...
    def __len__(self) -> int: ...
    def __lt__(self, other: Traceback) -> bool: ...
    if sys.version_info >= (3, 11):
        def __gt__(self, other: Traceback) -> bool: ...
        def __ge__(self, other: Traceback) -> bool: ...
        def __le__(self, other: Traceback) -> bool: ...
    else:
        def __gt__(self, other: Traceback, NotImplemented: Any = ...) -> bool: ...
        def __ge__(self, other: Traceback, NotImplemented: Any = ...) -> bool: ...
        def __le__(self, other: Traceback, NotImplemented: Any = ...) -> bool: ...

class Snapshot:
    def __init__(self, traces: Sequence[_TraceTupleT], traceback_limit: int) -> None: ...
    def compare_to(self, old_snapshot: Snapshot, key_type: str, cumulative: bool = ...) -> list[StatisticDiff]: ...
    def dump(self, filename: str) -> None: ...
    def filter_traces(self, filters: Sequence[DomainFilter | Filter]) -> Snapshot: ...
    @staticmethod
    def load(filename: str) -> Snapshot: ...
    def statistics(self, key_type: str, cumulative: bool = ...) -> list[Statistic]: ...
    traceback_limit: int
    traces: Sequence[Trace]
