import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = list(map(chr, range(97, 123)))

readpath = "C:\\Users\\Vishant\\Desktop\\py scripts\\scarlet.txt"
outpath = "C:\\Users\\Vishant\\Desktop\\py scripts\\newfile.csv"

file = open(readpath)
text = file.read()

# print(text[:100])
# print(type(text))
counter = {}
for chr in text:
    sm = chr.lower()
    if sm not in counter:
        counter[sm] = 0
    counter[sm]+=1

dict_to_tuple = list(counter.items())
list_keys=[]
list_values=[]


for element in dict_to_tuple:
    if element[0] in a:
        list_keys.append(element[0])
        list_values.append(element[1])

df = pd.DataFrame({'char':list_keys, 'values': list_values})
# df.reset_index(drop=True, inplace=True)
# print(df.head(5))
# df.to_csv(outpath,index=False)

df.drop(['char'], axis=1, inplace=True)

stddev = df.std()
mean = df.mean()