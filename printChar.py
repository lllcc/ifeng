def pn():
    dgt = []
    num = []
    c = 0
    for c in range(2 ** 16):
        ch = chr(c)
        if ch.isdigit(): dgt.append(ch)
        if ch.isnumeric(): num.append(ch)
    print('digit:', dgt)
    print('numeric', num)


pn()
