from enum import Enum
from typing import TypedDict, Dict

from typing_extensions import TypeAlias

from const import FileStatus


class FileType(Enum):
    ERP = "ERP"
    TRD = "TRD"


class HistoryFile(TypedDict):
    path: str
    name: str
    type: FileType
    status: FileStatus


FileHistory: TypeAlias = Dict[str, HistoryFile]

