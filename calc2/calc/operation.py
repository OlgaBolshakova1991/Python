def op(strr):
    if 'j' not in strr:
        some_list = strr.split()
        a = float(some_list[0])
        b = float(some_list[2])
        oper = some_list[1]
        return a, b, oper
    else:
        some_list = strr.split()
        a1 = some_list[0]
        a2 = ''.join(some_list[1:3])[:-1]
        b1 = some_list[4]
        b2 = ''.join(some_list[5:])[:-1]
        oper = some_list[3]
        a = complex(int(a1), int(a2))
        b = complex(int(b1), int(b2))
        return a, b, oper




