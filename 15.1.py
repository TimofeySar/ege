m = set()
for a1 in range(1,150):

    for a2 in range(a1+1, 151):
        flag = True
        for x in range(150):
            if not((25 <= x <= 64) <= (((40<=x<=115) and (not (a1 <= x <= a2))) <= (not(25 <= x <= 64)))):
                flag = False

        if flag:
            m.add(a2 - a1)
print(sorted(m))