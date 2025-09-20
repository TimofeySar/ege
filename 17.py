f = open("17_17558.txt").readlines()
a = []
for i in f:
    a.append(int(i))
t = len([i for i in range(len(a)) if a[i] % 32 == 0])
sh = 0
mm = 0
for i in range(0, len(a) - 1):
    if a[i] < 0 or a[i+1]< 0:
        if a[i] + a[i+1] < t:
            sh += 1
            mm = max(a[i] + a[i+1], mm)
print(sh, mm)
