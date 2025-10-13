f = [list(map(int, i.split())) for i in open("09.txt")]
c = 0
for i in range(len(f)):
    flag = False
    a = f[i]
    q = set(a)
    if len(q) == 6:
        min = set()
        max = set()
        for j in range(6):
            if not(a.count(a[j]) == 1 or a.count(a[j]) == 2):
                flag = True
                break
            if a.count(a[j]) == 2:
                max.add(a[j])
            if a.count(a[j]) == 1:
                min.add(a[j])
        if not flag:
            if sum(max) < sum(min):
                c += 1
print(c)


