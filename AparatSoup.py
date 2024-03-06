from bs4 import BeautifulSoup
import utilities

# AparatSoup word is combination of Aparat(website which we work on) and BeautifulSoup
# AparatSoup is responsible for all information we need to know about live
class AparatSoup:

    # initialize class and parameters
    def __init__(self, page_source):
        try:
            if utilities.check_page_source(page_source):
                self.page_source = page_source
                self.soup = BeautifulSoup(self.page_source, 'html.parser')
                self._live_users()
                self.chats = self._get_chats()
        except Exception as ex:
            print(ex)
    
    def _live_users(self):
        self.live_users_count = self.soup.find('span', {"class": 'liveCount_online_users'}).text
    
    def _get_chats(self):
        chats = []
        messages_div = self.soup.find_all('div', class_='message')
        
        for message in messages_div:
            
            # Maybe aparat add new types of chat columns or maybe someone send ruby and etc. this
            # if tests of code prevents such message causes crash. so unsupported messages may have
            # incomplete username or message text when we look at the object
            user_name = None
            if message.find('span', {'class': 'message__username'}):
                user_name = message.find('span', {'class': 'message__username'}).text.replace(":", "")

            message_text = None
            if message.find('div', {'class': 'message__text'}):
                message_text = message.find('div', {'class': 'message__text'}).text

            # if message is not replayed to anyone this goes to be None
            replayed_to_username = None
            if message.find('div', {'class': 'replay-user'}):
                replayed_to_username = message.find('div', {'class': 'replay-user'}).text 

            replayed_to_message = None
            if message.find('span', {'class': 'replay-text'}):
                replayed_to_message = message.find('span', {'class': 'replay-text'}).text 
            
            chats.append(Chat(user_name, message_text, replayed_to_username, replayed_to_message))

        return chats
    

class Chat():
    
    def __init__(self, user_name, message_text, replayed_to_username, replayed_to_message):
        self.user_name = user_name or "Empty"
        self.message_text = message_text or "Empty"
        self.replayed_to_username = replayed_to_username or "Empty"
        self.replayed_to_message = replayed_to_message or "Empty"

    def __eq__(self, __value: object) -> bool:

        if (self.user_name == __value.user_name and
            self.message_text == __value.message_text and
            self.replayed_to_message == __value.replayed_to_message and
            self.replayed_to_username == __value.replayed_to_username):

            return True
        else:
            return False