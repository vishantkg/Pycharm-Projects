from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random


#X-Paths for the various elements on login page
class Loginpage:
    username_text_area = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    password_text_area = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    notnowbutton = '//*[@class="sqdOP yWX7d    y3zKF     "]'
    notnownotifbutton = '//*[@class="aOOlW   HoLwm "]'
    instagramheadericon = '//*[@class="s4Iyt"]'

    # Login Credentials
    # username = input('Enter your Username ')
    # password = input('Enter your Password ')

    def __init__(self):
        pass

    def login(self ,username, password, chrome):
        usern = chrome.find_element_by_xpath(self.username_text_area)
        passw = chrome.find_element_by_xpath(self.password_text_area)
        usern.send_keys(username)
        time.sleep(random.randrange(1, 3))
        passw.send_keys(password)
        time.sleep(random.randrange(1, 3))

        #clicking the ENTER button 
        passw.send_keys(Keys.RETURN)
        time.sleep(random.randrange(3,4))

        try:
            chrome.find_element_by_xpath(self.notnowbutton).click()
            time.sleep(random.randrange(3,4))
            chrome.find_element_by_xpath(self.notnownotifbutton).click()
            time.sleep(random.randrange(3,4))
            chrome.find_element_by_xpath(self.instagramheadericon).click()
            time.sleep(random.randrange(3,4))
        except:
            pass
