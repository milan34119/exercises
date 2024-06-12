import re

def valid_student_id(string):
    return re.fullmatch('[rRsS][0-9]{7}', string)