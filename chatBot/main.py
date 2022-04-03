# from Getting_Images import getimage_url
# from Message_friend import *
import sys
sys.path.append("C:\\Users\\Vishant\\PycharmProjects\\chatBot\\")
sys.path.append("C:\\Users\\Vishant\\PycharmProjects\\chatBot\\Pages\\")
from Loginpage import *
from selenium import webdriver
from Base import *


# imgurl = getimage_url()
# chrome = webdriver.Chrome(executable_path="C:\\Users\\Vishant\\Downloads\\chromedriver_win32\\chromedriver.exe")
# chrome.get(getimage_url())
# time.sleep(10)

username = 'nomadsapien'
password = 'Hello@123'
chrome = openurl()
loginpage = Loginpage()
loginpage.login(username, password, chrome)
comment = 
