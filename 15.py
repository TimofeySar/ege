for a in range(1000, 1, -1):
    flag = True
    for x in range(1000):
        if not((x%a == 0) or ((70<=x<=90)<=(not(x%22 == 0)))):
            flag = False
    if flag:
        print(a)
        break
            