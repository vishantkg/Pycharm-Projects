from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random




# starts a new chrome session
def openurl():
    global chrome
    url = 'https://instagram.com/'
    try:
        chrome = webdriver.Chrome(executable_path="C:\\Users\\Vishant\\Downloads\\chromedriver_win32\\chromedriver.exe")
        chrome.get(url)
        chrome.maximize_window()
        time.sleep(random.randrange(3,4))
    except Exception as e:
        print('could not oprn the homepage, Error: ',e)

    return chrome
