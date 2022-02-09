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

    # finds the username box
    usern = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

    # sends the entered username
    usern.send_keys(username)
    time.sleep(random.randrange(1, 3))
    # finds the password box
    passw = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

    # sends the entered password
    passw.send_keys(your_password)
    time.sleep(random.randrange(1, 3))
    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    time.sleep(random.randrange(3,4))

    #finding Not Now buttons
    # chrome.find_element_by_class_name("yWX7d").click()
    # time.sleep(3)
    # chrome.find_element_by_class_name("aOOlW").click()
    # time.sleep(0.5)

    #opening friends profile
    chrome.get(url+friend)
    time.sleep(random.randrange(1,3))

    #finding message button
    # chrome.find_element_by_class_name("qF0y9").click()
    # time.sleep(random.randrange(1, 3))
    chrome.find_element_by_class_name("sqdOP").click()
    time.sleep(random.randrange(1, 3))

    #clicking the notnow button
    notnow = chrome.find_element_by_class_name('aOOlW   HoLwm ')
    notnow.click()
    time.sleep(random.randrange(1,2))
    
    #clicking image icon
    chrome.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/button[1]').click()
    time.sleep(random.randrange(1,2))

    # #clicking select from computer button
    # chrome.find_element_by_class_name('sqdOP')
    # time.sleep(random.randrange(1,2))

    # chrome.close()
