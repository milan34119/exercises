import re

def parse_link(string):
    # <a href="...">...</a>
    match = re.fullmatch('<a href="(.+)">(.*)</a>')
    
    if match:
        link, caption = match.groups
        return (link, caption)
    else:
        return None