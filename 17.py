f = open('17.txt').readlines()
a = list(map(int, f))
su = 0
sh =  0
for i in range(0, len(a) - 1):
    if a[i] % 3 == 0 or + a[i+1] % 3 == 0:
        sh += 1
        su = max(su, a[i] + a[i+1])
print(sh, su)
