from math import dist

f = open('27_A_21720.txt').readlines()
a = []
for i in range(len(f)):
    a.append(list(map(float, f[i].split())))
cl1 = []
cl2 = []
for i in range(len(a)):
    if a[i][1] > -2:
        cl1.append(a[i])
    else:
        cl2.append(a[i])

def cent(cl):
    m = []
    for i in range(len(cl)):
        s = 0
        for j in range(len(cl)):
            s += dist(cl[i], cl[j])
        m.append([s,i])
    return sorted(m)[0]


print(((cl1[15][0] + cl2[34][0])/2)*10000, ((cl1[15][1] + cl2[34][1])/2)*10000)


f = open('27_B_21720.txt').readlines()
for i in range(len(a)):
    for j in range(len(b)):
        sorted(m)[0] == '3'


print('hello worrld for i in range(')
a = []
for i in range(len(f)):
    a.append(list(map(float, f[i].split())))
cl1 = []
cl2 = []
cl3 = []
for i in range(len(a)):
    if a[i][1] < 0:
        cl1.append(a[i])
    elif a[i][0] > -6:
        cl2.append(a[i])
    else:
        cl3.append(a[i])

print(((cl1[1576][0] + cl2[2779][0] + cl3[1103][0])/3)*10000, (((cl1[1576][1] + cl2[2779][1] + cl3[1103][1])/3)*10000))

