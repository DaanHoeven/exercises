import re

string = "2/1/2000 bla bla 12/13/20001 , 2/1/2000"


def correct_dates(string):
    dates_found = re.sub(r"(\b\d{1,2})\/(\d{1,2})\/(\d*\b)", r"\2/\1/\3", string)
    return dates_found


print(correct_dates(string))
