import os
import json

def finduser(path, search):
    # search = 'bhai tera dance mast h lekin'
    flag = False
    name =[]
    try:
        f = open(path + "\\message_1.json")
        data = json.load(f)

    except Exception as e:
        print(f'{e}, could not load data')
        return 'Not found'

    for i in range(len(data['messages'])):
        msg = data['messages'][i]
        try:
            if search == msg['content']:
                flag = True
                name = msg['sender_name']
                break

        except:
            pass

    if flag==True:
        return name
    else:
        return 'Not found'



while True:
    search = input('Enter the message:')
    if search == '':
        break
    basepath="C:\\Users\\Vishant\\PycharmProjects\\insta\\inbox"
    path=""
    os.chdir(basepath)
    # print(os.getcwd())
    a = os.listdir()
    f = [a[a.index('shreyk_aev0ytxnwq')]]

    result = []
    folder = []
    #
    for i in range(len(a)):
        path = basepath+"\\"+a[i]
        result = finduser(path, search)
        if result != 'Not found':
            print(f"We got the mf, This was sent by {result}")
            break
        elif ((result == 'Not found') and (i == len(a)-1)):
            print('mf not found')