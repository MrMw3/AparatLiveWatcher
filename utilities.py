import re


def validate_url(url):

    if url == "" or url == None:
        return False
    
    elif re.match(r'https\:\/\/www\.aparat\.com\/([A-Za-z0-9_]*)\/live\/chat', url):
        return True
    
    else:
        return False