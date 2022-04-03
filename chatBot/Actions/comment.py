from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from time import sleep
import random

# from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui













url = 'https://instagram.com/'

# starts a new chrome session
def path():
    global chrome
    chrome = webdriver.Chrome(executable_path="C:\\Users\\Vishant\\Downloads\\chromedriver_win32\\chromedriver.exe")

#Function to enter the URL of the page
def url_name(url):
    chrome.get(url)
    sleep(random.randrange(3,4))

#Function to login to instagram
def comment(msg,count):
    username = 'nomadsapien'
    your_password = 'Hello@123'
    path()
    url_name(url)

    # finds the username box
    usern = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

    # sends the entered username
    usern.send_keys(username)
    sleep(random.randrange(1, 3))
    # finds the password box
    passw = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

    # sends the entered password
    passw.send_keys(your_password)
    sleep(random.randrange(1, 3))
    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    sleep(random.randrange(3,4))

    #finding Not Now buttons
    # chrome.find_element_by_class_name("yWX7d").click()
    # sleep(3)
    # chrome.find_element_by_class_name("aOOlW").click()
    # sleep(0.5)

    #opening sliceit post
    chrome.get('https://www.instagram.com/p/CaFDNkSBh1I/')
    sleep(random.randrange(5,6))
    i=0
    while i<count:
        
        comment_area = chrome.find_element_by_class_name("Ypffh")
        comment_area.click()
        sleep(random.randrange(1,3))
        comment_area = chrome.find_element_by_class_name("Ypffh")
        comment_area.click()
        comment_area.send_keys(msg)
        comment_area.submit()
        sleep(random.randrange(4,5))
        i+=1

    chrome.close()


comment("meee",100)