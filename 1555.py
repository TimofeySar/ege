sh = []
for al in range(1, 300):

    for ar in range(al, 300):
        flag = True
        for x in range(1, 200):
            if (25 <= x <= 64) <= (((40 <= x <= 115) and (not (al <= x <= ar))) <= (not (25 <= x <= 64))):
                pass
            else:
                flag = False

        if flag:
            sh.append(ar - al)

print(min(sh))
