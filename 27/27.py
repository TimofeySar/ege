from math import dist

a = open('27_A_23284.txt').readlines()
f = []
for i in range(len(a)):
    if a[i][0] == 'X':
        continue
    f.append(list(map(float, a[i].replace(',', '.').split())))
cl1 = []
cl2 = []
for i in range(len(f)):
    if f[i][1] < 15:
        cl1.append(f[i])
    else:
        cl2.append(f[i])


def cent(cl):
    m = []
    for i in range(len(cl)):
        s = 0
        for j in range(len(cl)):
            s += dist(cl[i], cl[j])
        m.append([s, i])
    return sorted(m)[0]


print(int((cl1[67][0] + cl2[109][0]) * 10000), int((cl1[67][1] + cl2[109][1]) * 10000))

a = open('27_B_23284.txt').readlines()
f = []
for i in range(len(a)):
    if a[i][0] == 'X':
        continue
    f.append(list(map(float, a[i].replace(',', '.').split())))
cl1 = []
cl2 = []
cl3 = []
for i in range(len(f)):
    if 0 < f[i][0] < 35:
        if f[i][0] < 10:
            cl1.append(f[i])
        elif f[i][0] < 20:
            cl2.append(f[i])
        else:
            cl3.append(f[i])


def cent(cl):
    m = []
    for i in range(len(cl)):
        s = 0
        for j in range(len(cl)):
            s += dist(cl[i], cl[j])
        m.append([s, i])
    return sorted(m)[0]


a = (cl1[126])
b = (cl2[50])
c = (cl3[22])

q = dist(a, b)
w = dist(a, c)
e = dist(c, b)
print(int(min(q, w, e) * 10000), int(max(q, w, e) * 10000))