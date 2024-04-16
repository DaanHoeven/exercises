import re


def is_valid_email_address(string):
    return re.fullmatch(r"[^A-Z]*@((student.ucll.be)|(ucll.be))", string)
