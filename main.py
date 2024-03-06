from selenium import webdriver
import utilities
import time

def main():
    #initialize driver
    try:
        driver = webdriver.Edge()
    except Exception:
        raise Exception("Failed to initialize webdriver make sure you have right driver in program Path.")

    # TODO: get url from user
    # url of live chat. ex: https://aparat.com/ana_ghaem/live/chat
    live_url = 'https://www.aparat.com/mehtiyt/live/chat'
    # it's time to check entered url validation
    if utilities.validate_url(live_url) is False:
        raise Exception("There is a problem with your entered link, check it and try again.")

    # Go and get page source
    try:
        driver.get(live_url)
        # i need the page source so check it's availability

        assert driver.page_source is not None or driver.page_source != ""
        print("[+] Page Loaded Successfully.")

        # Prevent console from being closed when driver do his job
        input()
    except Exception:
        raise Exception("An error occur when trying to get url. make sure url is in right format. ex: https://aparat.com/ana_ghaem/live/chat")




if __name__ == "__main__":
    main()