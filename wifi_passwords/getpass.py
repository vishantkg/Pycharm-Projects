import subprocess
import pandas as pd

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if 'All User Profile' in i]
searchterm = input('Enter the name of the wifi you want to search:')

for name in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile',name,'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        if searchterm.upper() in name.upper():
            print("{:<30}|  {:<}".format(name,results[0]))
        else:
            pass
    except IndexError:  
        print("{:<30}|  {:<}".format(name,""))


