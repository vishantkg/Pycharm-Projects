#given an integer, convert it to roman number
def quotient(n):
    num1 = [1000, 500, 100, 50, 10, 5, 1]
    qt,i = 0,0
    while True:
        qt = int(n/num1[i])
        if qt>=1:
            break
        i += 1
    key = num1[i]
    return qt,key;


def solution(num):
    if num == 0:
        return num
    rdict = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    num1 = [1, 5, 10, 50, 100, 500, 1000]
    roman = ""
    while num>0:
        if(num!=9):
            qt,key = quotient(num)
            if qt<=3:
                for i in range(qt):
                    roman = roman + rdict[key]
            elif qt>3:
                oldkey = key
                newkey = num1[num1.index(oldkey) + 1]
                roman = roman + rdict[oldkey]+rdict[newkey]
            num = num-qt*key
        else:
            roman = roman+"IX"
            break
    return roman

print(solution(79))