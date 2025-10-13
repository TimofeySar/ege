f = open("17-1.txt").readlines()
a = list(map(int, f))
amax = max([i for i in a if i % 10 == 7])
sh = 0
tmax = 0
for i in range(0, len(a) - 2):
    tr = [a[i], a[i+1], a[i+2]]
    if (len(str(tr[0])) == 3 and tr[0]%10 == 7) or( len(str(tr[1])) == 3  and tr[1]%10 == 7 )or (len(str(tr[2])) == 3 and tr[2]%10 == 7):
        if str(abs(tr[0]))[0] == str(abs(tr[1]))[0] == str(abs(tr[2]))[0]:
            if abs(sum(tr)) < amax:
                sh += 1
                tmax = max(tmax, abs(sum(tr)))

print(sh, tmax)
