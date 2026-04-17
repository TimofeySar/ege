# from itertools import product
#
# # words = [''.join(i) for i in list(product('АВЕНС', repeat=4))]
# k = 0
# ka = 0
# kt = 0
# sh=0
# for s in product('АСТЕК', repeat=8):
#     sh+=1
#     k += 1
#     i = ''.join(s)
#     if i == 'АТТЕСТАТ':
#         ka = k
#
#     if "ТЕСАК" in i: #if i == 'ТЕСАК': Keklol AHHAHAH
#         f = 0
#         for u in range(7):
#             if i[u] != i[u + 1]:
#                 f += 1
#         if f == 7:
#             kt = k
#
# print(ka - kt)
# print(sh)



from itertools import product

# words = [''.join(i) for i in list(product('АВЕНС', repeat=4))]
k = 0

for s in product('0234567', repeat=5):
    i = ''.join(s)
    if i[0] != "0":
        if len(set(i)) == 5:
            k1 = 0
            for u in range(4):
                if (int(i[u]) + int(i[u + 1])) % 2 != 0:
                    k1 += 1
            if k1 == 4:
                k += 1


print(k)

