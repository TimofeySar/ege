f = open('9.txt').readlines()
a = [list(map(int, f[i].split())) for i in range(len(f))]
sh = 0
for i in range(len(a)):
    q = set(a[i])
    if len(q) == 4 and(a[i].count(a[i][1]) == 3 or a[i].count(a[i][0]) == 3 or \
            a[i].count(a[i][2]) == 3 or a[i].count(a[i][3]) == 3 or\
            a[i].count(a[i][4]) == 3 or a[i].count(a[i][5]) == 3 ):
        w = sum(a[i])
        e = sum(list(q))
        if (((w - e)//2) *3) ** 2 > (e - (w - e)//2) **2:
            sh += 1
print(sh)