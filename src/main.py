from argparse import ArgumentParser

from core.check_file import check_file
from interface.errrors import dump_errors
from utils.art import display_art

if __name__ == '__main__':

    display_art("HJXH", by="line", leading=2)

    parser = ArgumentParser()

    parser.add_argument("-e", "--print_errors", help="打印所有错误类型", action="store_true")
    parser.add_argument("-c", "--check_file", help="检查待分析文件")

    args = parser.parse_args()

    if args.print_errors:
        dump_errors()

    if args.check_file:
        check_file(args.check_file)

    print("\n=== finished ===")
