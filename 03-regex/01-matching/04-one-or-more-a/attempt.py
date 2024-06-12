import re

def one_or_more_a(string):
    re.fullmatch('a+', string)