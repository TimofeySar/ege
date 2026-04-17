from math import dist

f = open('27_A-1.txt').readlines()
a = []
for line in f:
    a.append(list(map(float, line.split())))
cl1 = []
cl2 = []
for i in range(0,len(a)):
    if a[i][1] > 13:
        cl1.append(a[i])
    else:
        cl2.append(a[i])
def cent(cl):
    mas = []
    for i in range(len(cl)):
        s = 0
        for j in range(len(cl)):
            s += dist(cl[i], cl[j])
        mas.append([s, i])
    return sorted(mas)[0]
print(cent(cl1))
print(cent(cl2))
print((cl1[62][0] + cl2[68][0])*10000)
print((cl1[62][1] + cl2[68][1])*10000)
