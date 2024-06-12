import re

def negate_a(string):
    return re.fullmatch('[^a]*', string)