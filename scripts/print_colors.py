from termcolor import colored, COLORS

COLORS_FROM_NUM = dict((j - 30, i) for (i, j) in COLORS.items())
print(COLORS_FROM_NUM, end="\n\n\n")


def get_color(k):
    color = COLORS_FROM_NUM[k % COLORS.__len__() or 1]
    return color


import sys

with open(sys.argv[1]) as f:
    # for line in f:
    for (i, c) in enumerate(f):
        print(colored(c, get_color(i)), end="")
