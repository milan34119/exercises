import re 

def is_dna(string):
    re.fullmatch('G|A|T|C', string)