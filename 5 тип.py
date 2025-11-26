# s = int("46307921",29) + int("82410153",29)
# for x in range(1000):
#     su = s+x*29**3+x*29**4
#     if su%28==0:
#         print(su//28)

for n in range(200):
    a = bin(n)[2:]
    if n %5 == 0:
        a += '11'
    else:
        a += bin(n//5)[2:]
    r = int(a, 2)
    if r % 2 != 0 and r > 783:
        print(n)
        break