import re


def contains_three_digits(string):
    return re.match("(0|1|2|3|4|5|6|7|8|9)...*", string)
