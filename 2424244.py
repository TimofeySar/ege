delittl = ['AB', 'AC', 'AD', 'AF', 'EB', 'EC', 'ED', 'EF']
f = open('24.txt'). readline()
sh = 0
mm = []
mas = []
for i in range(len(f) - 1):
    if f[i:i+2] in delittl:
        mas.append(sh)
        sh = -1
    else:
        sh += 1
s = 0
for i in range(len(mas)- 131):
    for j in mas[i:i+132]:
        s += j
    mm.append(s + 130*2)
    s = 0
print(sorted(mm, reverse=True)[0])

