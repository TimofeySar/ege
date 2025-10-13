s = int("46307921",29) + int("82410153",29)
for x in range(1000):
    su = s+x*29**3+x*29**4
    if su%28==0:
        print(su//28)