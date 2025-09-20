def f(x):
    s = ''
    if f == '0':
        return '0'
    while x != 0:
        x, r = divmod(x, 7)
        s = str(r) + s
    return s


a = 7 ** 91 + 7 ** 160
for i in range(2030, 0, -1):
    q = a - i
    m = f(q)
    if m.count('0') == 70:
        print(i)
        break
