f = list(map(int, open('17_24892.txt').readlines()))
mina = -12345
for i in range(len(f)):
    if f[i] <0 and len(str(f[i])) == 5 and f[i] % 9 == 0:
        mina = max(f[i],mina)
sh = 0
mm = 123213123456
for i in range(len(f)-1):
    if f[i] + f[i + 1] < max(f[i], f[i +1]) and  max(f[i], f[i +1]) >= 0:
        if f[i] + f[i+1] > mina:
            sh +=1
            mm = min(f[i]**2 + f[i+1]**2, mm)
print(sh, mm)


чё