def solution(l):
    l.sort(reverse = True)
    sumof= sum([int(i) for i in l])
    digits = len(l)
    flag = False
    rem = sumof%3
    if(rem==0):
        num = 0
        for i in l:
            num = i + num*10
        return num
    else:
        for i in range(2):
            if(i == 1):
                last = l.pop()
                rem = last%3
            for j in range(len(l)-1,-1,-1):
                if(l[j]%3==rem):
                    remove_num = l[j]
                    l.remove(remove_num)
                    flag = True
                    break
            if(flag == True):
                num = 0
                for i in l:
                    num = i + num*10
                return num




# l = [1,4,3,1,5,9]
l=[9,3,4,5,5]
print(solution(l))