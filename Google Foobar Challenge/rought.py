import numpy as np


def solution(start,length):
    #make the array of numbers starting from the start
    arr = np.ones([length,length], dtype = np.int32, order = 'f')
    for i in range(length):
        for j in range(length):
            arr[i][j]=start
            start+=1
    return arr

def xorop(row, row_length):
    #row is a list variable
    print(row)
    result=0
    start = row[0]
    if start%2==0: #start is even
        rem4=row_length%4
        q4=int(row_length/4)
        for a in range(rem4):
            result = result^row[q4*4+a]

    else:
        row1=row[1:]
        row_length=row_length-1
        rem4 = row_length % 4
        q4 = int(row_length / 4)
        for a in range(rem4):
            result = result ^ row[q4 * 4 + a]
        result = result^row[0]
    return result

def slice(arr, length):
    #slicing the array by row
    row=[]
    checksum=0
    for i in range(length):
        row=list(arr[i,:])
        for m in range(i):
            row.pop()
        # print(row)
        checksum=checksum^xorop(row,length-i)
    return checksum

def start():
    start=int(input('Enter start: '))
    length=int(input('Enter length: '))
    arr=solution(start,length)
    checksum=slice(arr, length)
    print(f'Checksum= {checksum}')

start()

