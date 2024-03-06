from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import utilities
from AparatSoup import AparatSoup, Chat
import time

def main():
    #initialize driver
    try:
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        driver = webdriver.Edge(options)
    except Exception:
        raise Exception("Failed to initialize webdriver make sure you have right driver in program Path.")

    # TODO: get url from user
    # url of live chat. ex: https://aparat.com/tigo_blade/live/chat
    live_url = 'https://www.aparat.com/tigo_blade/live/chat'
    # it's time to check entered url validation
    if utilities.validate_url(live_url) is False:
        raise Exception("There is a problem with your entered link, check it and try again.")

    # Go and get page source
    try:
        driver.get(live_url)

        # i need the page source so check it's availability
        assert driver.page_source is not None and driver.page_source != ""
        print("[+] Page Loaded Successfully.")
        
        # ON each 1 second check for new messages
        while True:
            time.sleep(1)
            delay = 10
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'chat')))
            aparatSoup = AparatSoup(driver.page_source)
            users = aparatSoup.live_users_count
            print(f"-------- Online Users: {users} --------")

            for chat in aparatSoup.chats:
                if chat.user_name is not None:
                    if chat_already_exists(chat) is False:
                        db = utilities.DB()
                        db.insert_message(chat)
                        print('[+] Chat record inserted.')
                    else:
                        continue
                else:
                    continue

        
    except Exception:
        raise Exception("An error occur when trying to get url. make sure url is in right format. ex: https://aparat.com/tigo_blade/live/chat")

    # Prevent console from being closed when driver do his job
    input()


def chat_already_exists(chat):
    query_results = utilities.DB().get_last_50_records()
    for query_result in query_results:
        old_chat = Chat(*query_result)
        if old_chat == chat:
            return True
    return False


if __name__ == "__main__":
    main()