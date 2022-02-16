import csv
import os
from typing import List

from termcolor import colored

from const import FileStatus
from errrors import MyError, VALID_FILE_SUFFIXES, VALID_FILE_PREFIXES, TARGET_ERP_FIELDS, TARGET_TRD_FIELDS
from log import my_logger
from utils import print_ok, print_error, read_history, dump_history
from interface import FileType


def get_file_type(fn: str) -> FileType:
    prefix = fn.strip()[:3].upper()
    if prefix not in VALID_FILE_PREFIXES:
        print_error(f"file prefix must be in {VALID_FILE_PREFIXES}, but got {prefix}")
        raise Exception(MyError.FILE_PREFIX_INVALID)
    print_ok(f"file prefix valid: [{prefix}]")
    return FileType.ERP if fn[:3].upper() == "ERP" else FileType.TRD


def get_target_fields(ft: FileType) -> List[str]:
    return TARGET_ERP_FIELDS if ft == FileType.ERP else TARGET_TRD_FIELDS


def check_file(fp: str):
    my_logger.info(f"checking file: <{fp}>")
    fn = os.path.basename(fp).strip()
    print(f"--- checking file: {colored(fn, 'yellow')}")

    if not os.path.exists(fp):
        print_error(f"file not exist: [{fp}]")
        raise Exception(MyError.FILE_NOT_EXIST.value)
    print_ok(f"file exist: [{fp}]")

    file_suffix = os.path.splitext(fp)[-1]
    if file_suffix not in VALID_FILE_SUFFIXES:
        print_error(f"file suffix must be in {VALID_FILE_SUFFIXES}, but got {file_suffix}")
        raise Exception(MyError.FILE_SUFFIX_INVALID.value)
    print_ok(f"file suffix valid: [{file_suffix}]")
    del file_suffix

    # 这个判断是否已经分析过的逻辑，可要可不要
    h = read_history()
    if h.get(fn, {}).get("status") == FileStatus.MARK_FINISHED:
        print_error(f"file has been parsed and marked as finished")
        raise Exception(MyError.FILE_DUPLICATED.value)
    # print_ok("file valid: it's not duplicated") # 这句感觉没必要打印
    h.update({fn: {"status": FileStatus.UNKNOWN.value}})
    dump_history(h)

    file_type = get_file_type(fn)
    target_fields = get_target_fields(file_type)

    for encoding in ["utf-8", "gbk"]:
        my_logger.info(f"trying to parse file using encoding: [{encoding}]")
        with open(fp, encoding=encoding) as f:
            reader = csv.reader(f)  # see: - [csv — CSV File Reading and Writing — Python 3.10.2 documentation](https://docs.python.org/3/library/csv.html)
            line = 0
            try:
                row = reader.__iter__().__next__()
                print_ok(f"encoding verified: [{encoding}]")

                my_logger.info({"head row": row})
                for target_field in target_fields:
                    if target_field not in row:
                        print_error(f"failed to find target field of [{target_field}] in head row of {row}")
                        raise Exception(MyError.TABLE_HEAD_ROW_INVALID.value)
                else:
                    print_ok(f"head row valid: {row}")
                    break
            except UnicodeDecodeError:
                continue
            except csv.Error as e:
                print({"line": line})
                raise e
    else:
        raise Exception(MyError.FILE_ENCODING_INVALID.value)
