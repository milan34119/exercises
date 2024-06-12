import re

def is_valid_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?')

    if match:
        # hours = match[1]
        # minutes = match[2]
        # seconds = match[3]
        # milliseconds = match[4] or '.000'
        h, m, s, ms = match.groups()
        ms = ms or '.000'
    else:
        return None