f = open('17_23757.txt').readlines()
a = list(map(int, f))
amin = 9999999
for i in range(len(a)):
    if len(str(a[i])) == 2:
        amin = min(a[i], amin)

sh = 0
mm = 0
for i in range(0, len(a)-1):
    if len(str(a[i])) == 2 and len(str(a[i+1])) != 2:
        if (a[i] + a[i+1]) % amin == 0:
            sh += 1
            mm = max(mm, a[i] + a[i+1])
    if len(str(a[i])) != 2 and len(str(a[i+1])) == 2:
        if (a[i] + a[i+1]) % amin == 0:
            sh += 1
            mm = max(mm, a[i] + a[i + 1])

print(sh, mm)