import re

def only_vowels(string):
    re.fullmatch('(a|e|o|u|i|)*', string)