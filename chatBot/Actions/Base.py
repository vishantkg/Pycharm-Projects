from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random

# Login Credentials
# username = input('Enter your Username ')
# password = input('Enter your Password ')

url = 'https://instagram.com/'

# starts a new chrome session
def path():
    global chrome
    chrome = webdriver.Chrome(executable_path="C:\\Users\\Vishant\\Downloads\\chromedriver_win32\\chromedriver.exe")
    url_name(url)

#Function to enter the URL of the page
def url_name(url):
    chrome.get(url)
    time.sleep(random.randrange(3,4))

#Function to login to instagram
def sendMessage(friend, message_content = ""):
    username = 'nomadsapien'
    your_password = 'Hello@123'
    path()
    url_name(url)