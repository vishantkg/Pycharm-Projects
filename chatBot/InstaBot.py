import random
import time
import os
from instabot import Bot

# m = "C:\\Users\\Vishant\\PycharmProjects\\chatBot\\"
# for i in os.listdir(m):
#     if i == 'config':
#         os.unlink(m+i)

bot = Bot()
time.sleep(random.randrange(1,2))
bot.login(username='vishantkg', password='kaqWim-vechyg-0daghi')
# bot.login(username='nomadsapien', password='Hello@123')
time.sleep(6)
# bot.send_photo(filepath = "images/lok0D.jpg", user_ids='vishantkg')
bot.send_photo(filepath = "C:\\Users\\Vishant\\PycharmProjects\\chatBot\\images\\lok0D.jpg", user_ids='noamdsapien')
time.sleep(random.randrange(1,3))
bot.logout()