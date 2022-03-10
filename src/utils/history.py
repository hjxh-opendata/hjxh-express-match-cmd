import json
import os

from utils.paths import DATA_DIR
from interface.files import FileHistory

history = None


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