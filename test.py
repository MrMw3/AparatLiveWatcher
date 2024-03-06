from AparatSoup import AparatSoup, Chat
import sqlite3
import time
import utilities

with open('logs/source3.txt', 'r', encoding='utf-8') as file:
    source = file.read()
    aparatSoup = AparatSoup(source)
    aparatSoup.chats
    query_results = utilities.DB().get_last_30_records()
    old_chats = []
    for query_result in query_results:
        old_chat = Chat(*query_result)
        for chat in aparatSoup.chats:
            if old_chat == chat:
                print("Equal")
        


    