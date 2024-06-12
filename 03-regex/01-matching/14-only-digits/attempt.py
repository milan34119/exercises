import re

def only_digits(string):
    re.fullmatch('(0-9)*', string)