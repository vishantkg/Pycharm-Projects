def decimalTobase(dn, db):
    digits = []
    while dn > 0:
        digits.insert(0, str(dn % db))
        dn  =int(dn / db)
    return ''.join(digits)

def baseTodecimal(dn,db):
    temp = int(str(dn),db)
    return temp

def getsubtract(x,y,b):
    if b == 10:
        return int(x)-int(y)
    temp1 = baseTodecimal(x,b)
    temp2 = baseTodecimal(y,b)
    temp = temp1 - temp2
    return decimalTobase(temp,b)

def solution(n,b):
    listofID = [n]
    while True:
        x = "".join(sorted(str(n), reverse = True))
        y = "".join(sorted(str(n), reverse = False))
        z = getsubtract(x,y,b)

        zl = len(str(z))
        xl = len(str (x))
        if(zl!=xl):
            z = z* pow(10, (xl - zl))
        for a in listofID:
            if(a == z):
                m = len(listofID)-listofID.index(a)
                return m
                break
        listofID.append(z)
        n = z
    return x

print(solution(23873475,9))