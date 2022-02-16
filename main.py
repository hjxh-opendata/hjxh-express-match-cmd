import random
from argparse import ArgumentParser

from art import tprint, text2art
from art.art_param import FONT_MAP
from termcolor import colored, COLORS

from check_file import check_file
from errrors import dump_errors, MyError


def print_hello(s, by="char", leading=2):
    s = text2art(s, "alligator")
    print()
    if by == "char":
        print(" " * leading, end="")
        for (i, c) in enumerate(s):
            if c == "\n":
                print("\n", " " * leading, end="")
            else:
                print(colored(c, random.choice(list(COLORS))), end="")
    elif by == "line":
        # COLOR_LIST = 'red, magenta, blue, green, cyan, cyan, white, yellow'.split(", ")
        COLOR_LIST = 'red, magenta, blue, green, cyan, white, yellow'.split(", ")
        COLOR_LIST.reverse()
        for (i, line) in enumerate(s.splitlines()):
            print(" " * leading, colored(line, COLOR_LIST[i]))
            # print(" " * leading, colored(line, random.choice(list(COLORS))))
    else:
        for line in s.splitlines():
            print(" " * leading, line)
    print()


if __name__ == '__main__':
    print_hello("HJXH", by="line", leading=2)

    parser = ArgumentParser()

    parser.add_argument("-e", "--print_errors", help="打印所有错误类型", action="store_true")
    parser.add_argument("-c", "--check_file", help="检查待分析文件")

    args = parser.parse_args()

    if args.print_errors:
        dump_errors()
        exit()

    if args.check_file:
        check_file(args.check_file)

    print("\n=== finished ===")
