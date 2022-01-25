import os
import json

def finduser(path):
    # search = 'bhai tera dance mast h lekin'
    search = "how studious!"
    flag = False

    try:
        f = open(path + '\\message_1.json')
        data = json.load(f)
        print(json.dumps(data['messages'][:10], indent = 3))

        for msg in data['messages']:
            # print(msg['content'])
            if search in msg['content']:
                flag = True
                break

        if flag==True:
            return data['participants'][0]['name']
        else:
            return 'Not found'


    except Exception as e:
        print(f'{e}, file not present')
        return 'Not found'


basepath="C:\\Users\\Vishant\\PycharmProjects\\insta\\inbox"
path=''
os.chdir(basepath)
# print(os.getcwd())
a = os.listdir()
f = [a[a.index('shreyk_aev0ytxnwq')]]

result = []
folder = []
#
for i in range(len(f)):
    path = basepath+"\\"+f[i]
    print(f"path= {path}")
    result = finduser(path)
    if result != 'Not found':
        print(f"We got the mf, {result}")
        break
    elif 1==len(a)-1:
        print('mf not found')