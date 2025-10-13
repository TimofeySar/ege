for i in range(1, 100000000000000000):
    s = 0
    for k in range(1, i + 1):
        if i % k == 0:
            s = s + 1
    if s <= 2:
        print(i)
