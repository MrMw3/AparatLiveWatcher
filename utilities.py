import re
import os
import sqlite3
import time

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


class DB():

    def __init__(self):
        if os.path.exists('sqlite.db'):
            pass
        else:
            #build database
            print("[-] Database doesn't found,")
            self._build_database()
            self.__init__()
    
    def _build_database(self):
        try:
            dbconn = sqlite3.connect('sqlite.db')
            dbcursor = dbconn.cursor()
            dbcursor.execute("CREATE TABLE messages (id INTEGER PRIMARY KEY, username VARCHAR(255), message TEXT, replay_username VARCHAR(255), replay_message TEXT, time TIMESTAMP)")
            dbconn.close()
            print("[+] Database Created Successfully.")
        except Exception as ex:
            print(ex)

    def insert_message(self, chat):
        values = [chat.user_name, chat.message_text, chat.replayed_to_username, chat.replayed_to_message, time.time()]
        dbconn = sqlite3.connect('sqlite.db')
        dbcursor = dbconn.cursor()
        dbcursor.execute("INSERT INTO messages (username, message, replay_username, replay_message, time) VALUES (?, ?, ?, ?, ?)", values)
        dbconn.commit()
        dbconn.close()
        return True
    
    def get_last_50_records(self):
        dbconn = sqlite3.connect('sqlite.db')
        dbcursor = dbconn.cursor()
        results = dbcursor.execute("SELECT username, message, replay_username, replay_message from messages limit 50")
        return results.fetchall()
