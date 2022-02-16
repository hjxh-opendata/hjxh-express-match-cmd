# Python program to print
# colored text and background
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
    # style = 7
    # fg = 30
        for fg in range(10, 38):
            s1 = ''
            bg = 40
            for bg in range(10, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


print_format_table()

# red, magenta, blue, green, cyna, gray, white, yellow
# 1, 5, 4, 2, 6, 7, 8, 3