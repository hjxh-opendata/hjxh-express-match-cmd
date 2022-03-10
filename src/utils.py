import json
import os

from termcolor import colored

from base import DATA_DIR
from interface import FileHistory

history = None


def print_ok(s: str):
    print(colored("  √", "green"), s)


def print_error(s: str):
    print(colored("  X", "red"), s)


def get_history_file_path() -> str:
    return os.path.join(DATA_DIR, "history.json")


def read_history() -> FileHistory:
    """
    单例获取 `history`
    :return: 字典文件，记录每个读取的文件的信息
    """
    global history
    if history is None:
        history = dict()
        if os.path.exists(get_history_file_path()):
            history = json.load(open(get_history_file_path()))
    return history


def dump_history(h):
    global history
    history = h
    json.dump(h, open(get_history_file_path(), "w"), ensure_ascii=False, indent=2)