def decimalTobase(dn, db):
    '''Convert Desired No(dn) a positive number to desire Base(db)'''
    digits = []
    dn = int(dn)
    while dn > 0:
        digits.insert(0, str(dn % db))
        dn  =int(dn / db)
    return ''.join(digits)

def to_base_10(dn,db):
    temp = int(str(dn),db)
    return temp

def answer(n, b):

    k = len(n)
    m = n
    mini_id = []
    while m not in mini_id:
        mini_id.append(m)
        s = sorted(m)
        x_descend = ''.join(s[::-1])
        y_ascend = ''.join(s)
        if b == 10:
            int_m = int(x_descend) - int(y_ascend)
            m = str(int_m)
        else:
            int_m_10 = int(to_base_10(x_descend, b)) - int(to_base_10(y_ascend, b))
            m = decimalTobase(str(int_m_10), b)

        m =  (k - len(m)) * '0' + m
    return len(mini_id) - mini_id.index(m)


print(answer('210022',3))
print(answer('1211',10))
print(answer('124578',9))