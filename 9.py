f = [list(map(int, i.split())) for i in open("09.txt")]
c = 0
for i in range(len(f)):
    a = set(f[i])
    if len(a) == 4 and ((sum(f[i]) -max(f[i]))  > max(f[i])):
        c += 1
print(c)


# 13189