# rucoblud sanina ochlo bleduna vagina suka eblanushe vlagalishe perdun drochila pidor pizda tuz malofia anus vagina putana pidrila shalava mahonka elda
#
# #oleniy penis moy talesman vse vremia im zanat moy karmaaaan
#
# from fnmatch import *
# for i in range(0, 10**9, 23):
#     if fnmatch(str(i), '12345?7?8'):
#         print(i, i // 23)


def dell(n):
    m = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            m.append(i)
            m.append(n//i)
    return sorted(list(set(m)))

def prost(n):
    return n > 1 and all(n%d != 0 for d in range(2, int(n**0.5) + 1))


mas = []
for i in range(1000000, 1000020):
    if len(mas) < 5:
        m = dell(i)
        if len(m) == 3:
            mas.append([i, m[2]])
    else:
        break
print(mas)