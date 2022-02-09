#this is a working code


from selenium import webdriver

#import time module
import time

#creating driver object
driver=webdriver.Chrome(executable_path="C:\\Users\\Vishant\\Downloads\\chromedriver_win32\\chromedriver.exe")

#maximizing the window
driver.maximize_window()

#navigating to instagram page
driver.get("https://www.instagram.com/")

#delaying for 3 seconds so that the email and password boxes can load
time.sleep(3)

#creating id to store email
id="000000"

#passing email to email input box
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)

#creating password to store password
password="0000000"

#passing password to password input box
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()