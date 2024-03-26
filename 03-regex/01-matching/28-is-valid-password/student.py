# Write your code here
import re

def is_valid_password(string):
    return re.fullmatch('([+-*/\.*][a-z][A-Z][0-9])+{12}')