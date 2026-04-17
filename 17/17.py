# Доступен файл для чтения: 17.txt
f = []
ss = 0
m = 0
for i in open('17 (2).txt'):
  a = int(i)
  if a%11 == 0:
    ss += a
    m +=1
  f.append((a))
srz = ss//m
sh = 0
maxs = 0
for i in range(len(f)-2):
    if str(abs(f[i]))[-2:] == '11' or str(abs(f[i+1]))[-2:] == '11' or str(abs(f[i+2]))[-2:] == '11':
        if ((f[i]) +(f[i + 1]) + (f[i + 2]))//3 > srz:
            sh += 1
            maxs = max(((f[i]) +(f[i + 1]) + (f[i + 2])), maxs)
print(sh, maxs)