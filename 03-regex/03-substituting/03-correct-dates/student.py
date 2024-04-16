# Write your code here
import re


def correct_dates(string):
    return re.sub(r"(\d+)/(\d+)/(\d+)", r"\2/\1/\3", string)


print(correct_dates("1/2/3"))  # Output: 2/1/3
