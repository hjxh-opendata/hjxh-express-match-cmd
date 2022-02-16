from enum import Enum
from pprint import pprint

from termcolor import colored

VALID_FILE_SUFFIXES = (".csv",)

VALID_FILE_PREFIXES = ("ERP", "TRD", )

VALID_FILE_ENCODINGS = ("utf-8", "gbk", )

MAX_FILE_SIZE_MB = 50

TARGET_ERP_FIELDS = ("单号", "weight", "date", "area", "cp")
TARGET_ERP_FIELDS_EN = ("id", "weight", "date", "area", "cp")

TARGET_TRD_FIELDS = TARGET_ERP_FIELDS + ("fee", )
TARGET_TRD_FIELDS_EN = TARGET_TRD_FIELDS + ("fee", )


class MyError(str, Enum):
    """
    define all the error types
    """

    # ----------------------------
    # ERROR TYPE 1. FILE(WORKBOOK)
    # ----------------------------

    # 当用于上传某个文件，却为空时，引发该错误；属于检查文件是否存在的预执行动作
    FILE_NOT_EMPTY = "必须指定一个文件"

    # 当用户使用命令行去读取某文件，或者不小心改动了其参数，或是分隔符不正确，或是没有加引号之类，就会导致找不到文件
    FILE_NOT_EXIST = "文件不存在"

    # TODO: 用户已经处理过某文件（比如标记），则重新上传该文件，将报错
    FILE_DUPLICATED = "文件已处理"

    # 检查文件后缀，必须符合 `VALID_FILE_TYPES`
    FILE_SUFFIX_INVALID = "文件后缀不合规"

    # 由于系统的不同业务需要上传不同的文件，因此对文件名首先做一次规定
    FILE_PREFIX_INVALID = "文件前缀不合规"

    # 为防止文件过大，导致错误概率增加以及不方便管理，因此控制文件大小
    FILE_SIZE_INVALID = "文件大小不合规"

    # !IMPORTANT: 检查文件编码，必须符合 `VALID_FILE_ENCODINGS`
    FILE_ENCODING_INVALID = "文件编码不合规"

    # ----------------------------
    # ERROR TYPE 2. SHEET(PASS，由于我们只使用.csv，所以没有sheet级别的错误；如果是.xlsx，则会)
    # ----------------------------

    # ----------------------------
    # ERROR TYPE 3. TABLE
    # ----------------------------

    # 第一行（或者第一个非空行）里，需要有目标字段：`VALID_TABLE_HEAD_ROW_FILES`
    TABLE_HEAD_ROW_INVALID = "表抬头字段不合规"

    # 在按行解析表时，有时候会因为引号等问题，导致解析异常，这时需要报错
    TABLE_ROW_INVALID = "解析行异常"

    # ----------------------------
    # ERROR TYPE 4. FIELD
    # ----------------------------

    FIELD_ID_INVALID = "[单号]列异常"

    FIELD_WEIGHT_INVALID = "[重量]列异常"

    FIELD_DATE_INVALID = "[日期]列异常"

    FIELD_AREA_INVALID = "[地区]列异常"

    FIELD_FEE_INVALID = "[费用]列异常"

    FIELD_CP_INVALID = "[公司]列异常"


def dump_errors():
    """
    dump all the error types
    :return:
    """
    print(colored(">>> Dump All the Errors: ", "green", attrs=["bold", "blink"]))
    for (i, j) in MyError.__dict__['_member_map_'].items():
        print(f"error_type: {i:25}, error_name: {j.value}")
    print()


if __name__ == '__main__':
    dump_errors()
