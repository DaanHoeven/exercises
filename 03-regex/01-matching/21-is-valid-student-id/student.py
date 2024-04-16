import re


def is_valid_student_id(string):
    return re.fullmatch("(^r|^R|^S|^s)(0|1|2|3|4|5|6|7|8|9)......", string)
