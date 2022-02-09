import requests
import json

def getimages(tags_text='cat', num=1):
    url = 'https://api.flickr.com/services/rest'
    params = {}
    params['method'] = 'flickr.photos.search'
    params['format'] = 'json'
    params['api_key'] = '35449a818fcf5465886cf403be7bff61'
    params['per_page'] = num
    params['nojsoncallback'] = 1
    params['tags'] = tags_text
    params['media'] = 'photos'
    page = requests.get(url, params = params)
    data = json.loads(page.text)

    return data

def geturl(images):
    imgurl = 'https://www.flickr.com/photos/'
    for photo in images['photos']['photo']:
        print(f'{imgurl}{photo["owner"]}/{photo["id"]}')

#tags_text = Nanda Devi, Trishul, Mount Everest
tags_text = input('Enter the search term: ')
num = int(input('no. of images: '))
images = getimages(tags_text, num)
geturl(images)


