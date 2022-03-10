import random

from art import text2art
from colorama import init
from termcolor import colored, COLORS


def print_ok(s: str):
    print(colored("  √", "green"), s)


def print_error(s: str):
    print(colored("  X", "red"), s)


def display_art(s, by="char", leading=2):
    init()  # enable windows color output, ref: https://pypi.org/project/colorama/

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