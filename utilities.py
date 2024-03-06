import re


def validate_url(url):

    if url == "" or url == None:
        return False
    
    elif re.match(r'https\:\/\/www\.aparat\.com\/([A-Za-z0-9_]*)\/live\/chat', url):
        return True
    
    else:
        return False
    
def save_page_source(page_source):
    try:
        with open("logs/source.txt", encoding='utf-8') as file:
            file.write(page_source)
            print("[+] Page source saved in logs/source.txt Successfully/")
    except Exception as ex:
        print(ex)