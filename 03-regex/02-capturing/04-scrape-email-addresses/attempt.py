import re

def scrape_emails(string):
    return re.findall('[a-Z0-9]+@(gmail.com|hotmail.com|yahoo.be|telenet.be)', string)