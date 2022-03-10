from enum import Enum
from typing import TypedDict, Dict

from typing_extensions import TypeAlias


class FileStatus(Enum):
    UNKNOWN = "UNKNOWN"

    PARSE_ERROR = "PARSE_ERROR"

    PARSE_FINISHED = "PARSE_FINISHED"

    MARK_FINISHED = "MARK_FINISHED"


class FileType(Enum):
    ERP = "ERP"
    TRD = "TRD"


class HistoryFile(TypedDict):
    path: str
    name: str
    type: FileType
    status: FileStatus


FileHistory: TypeAlias = Dict[str, HistoryFile]
