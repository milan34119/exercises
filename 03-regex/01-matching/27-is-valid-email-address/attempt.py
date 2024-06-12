import re

def valid_email(string):
    return re.fullmatch(r'[a-z0-9]+@(student.ucll.be)|(ucll.be)', string)