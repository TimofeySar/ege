# rucoblud sanina ochlo bleduna vagina suka eblanushe vlagalishe perdun drochila pidor pizda tuz malofia anus vagina putana pidrila shalava mahonka elda
#
# #oleniy penis moy talesman vse vremia im zanat moy karmaaaan
#
# from fnmatch import *
# for i in range(10000000, 10**9, 23):
#     if fnmatch(str(i), '12345?7?8'):
#         print(i, i // 23)
#


def dell(n):
    m = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            m.append(i)

            m.append(n//i)
    return sorted(list(set(m)))

def prost(n):
    if len(dell(n)) == 2:
        return True

mas = []
for i in range(24517512, 400000000000):
    if len(mas) < 5:
        m = dell(i)
        if len(m) == 12:
            sh = 0
            for j in range(12):
                if prost(m[j]):
                    sh +=1
            if sh==12:
                mas.append(i)


    else:
        break
print(mas)