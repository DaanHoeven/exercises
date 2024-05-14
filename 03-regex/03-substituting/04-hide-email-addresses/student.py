import re


def hide_email_addresses(string):
    def replace(match):
        return "*" * len(match.group(0))

    patern = r"([a-zA-Z0-9.]+@[a-zA-Z]*[.][a-z]*)"
    return re.sub(patern, replace, string)
