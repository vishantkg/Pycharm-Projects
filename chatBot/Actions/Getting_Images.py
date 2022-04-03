''''This function does the following-
1. gets a random image from the internet,
2. eletes the previous images,
3. saves the new image to the folder,
4. returns and url of the image '''


import requests
import json
import urllib.request
import os


filepath = 'C:\\Users\\Vishant\\PycharmProjects\\chatBot\\images\\'
def getimage_url():
    clearfolder(filepath)

    url = 'https://aws.random.cat/meow?ref=public-apis'
    page = requests.get(url)
    response = json.loads(page.text)
    imgurl = response['file']

    lastindex = imgurl.rfind("/")
    filename = imgurl[lastindex+1:]
    fullpath = '{}{}'.format(filepath,filename)

    #downloading the image
    urllib.request.urlretrieve(imgurl,fullpath)

    return fullpath

#deletes the previous cat image
def clearfolder(path):
    for x in os.listdir(path):
        os.unlink(path+x)
