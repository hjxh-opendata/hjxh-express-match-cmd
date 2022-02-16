from enum import Enum


class FileStatus(Enum):

    UNKNOWN = "UNKNOWN"

    PARSE_ERROR = "PARSE_ERROR"

    PARSE_FINISHED = "PARSE_FINISHED"

    MARK_FINISHED = "MARK_FINISHED"
