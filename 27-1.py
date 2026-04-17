from math import dist

f = open('27_А.txt').readlines()
data = []
for i in range(len(f)):
    f[i] = f[i].replace(',', '.')
    data.append(list(map(float, f[i].split(' '))))
cl1 = []
cl2 = []
for i in range(len(data)):
    if data[i][1] > 1:
        cl1.append(data[i])
    else:
        cl2.append(data[i])


def cal(cl):
    mas = []
    for i in range(len(cl)):
        s = 0
        for j in range(len(cl)):
            s += dist(cl[i], cl[j])
        mas.append([s, i])
    return sorted(mas)[0]


print(((cl1[7][0] + cl2[49][0])/2)*10000)
print(((cl1[7][1] + cl2[49][1])/2)*10000)


f = open('27_Б.txt').readlines()
data = []
for i in range(len(f)):
    f[i] = f[i].replace(',', '.')
    data.append(list(map(float, f[i].split(' '))))
cl1 = []
cl2 = []
cl3 = []
for i in range(len(data)):
    if data[i][0] > 21:
        cl1.append(data[i])
    elif data[i][0] < 10:
        cl2.append(data[i])
    else:
        cl3.append(data[i])

print(((cl1[1801][0] + cl2[734][0] + cl3[1022][0])/3)*10000)
print(((cl1[1801][1] + cl2[734][1] + cl3[1022][1])/3) * 10000)


