import re


def validate_url(url):

    if url == "" or url == None:
        return False
    
    elif re.match(r'https\:\/\/www\.aparat\.com\/([A-Za-z0-9_]*)\/live\/chat', url):
        return True
    
    else:
        return False
    
def save_page_source(page_source, name):
    try:
        with open(f"logs/{name}.txt", "w", encoding='utf-8') as file:
            file.write(page_source)
            print(f"[+] Page source saved in logs/{name}.txt Successfully/")
    except Exception as ex:
        print(ex)

def check_page_source(page_source):
    if page_source is not None and page_source != "":
        return True
    else:
        raise Exception("Page source can't be empty or null")
