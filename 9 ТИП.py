# sp = [list(map(int, i.split())) for i in open("09.txt")]
# k = 0
# # print(sp)
# for i in sp:
#     pov = [x for x in i if i.count(x) == 3]
#     nepov = [x for x in i if i.count(x) == 1]
#     if len(pov) == 3 and len(nepov) == 4:
#         if (sum(nepov) / 4) <= (pov[0]):
#             k += 1
# print(k)

# sp = list(u for u in [list(map(int, i.split())) for i in open("09.txt")])
#
# k = 0
# print(sp)
# for i in sp:
#     print(i)
#     a = set(i)
#     if len(a)==5 and max(i) + min(i) <= sum(i) - (max(i) + min(i)):
#         k += 1
#
#
# print(k)

# for i in sp:
#     pov = [x for x in i if i.count(x) == 3]
#     nepov = [x for x in i if i.count(x) == 1]
#     if len(pov) == 3 and len(nepov) == 4:
#         if (sum(nepov) / 4) <= (pov[0]):
#             k += 1
# print(k)

# sp = [list(map(int, i.split())) for i in open("09.txt")]
# k = mx = 0
# # print(sp)
# for i in sp:
#     k += 1
#     # print(i)
#     pov = [x for x in i if i.count(x) == 3]
#     nepov = [x for x in i if i.count(x) == 1]
#     if len(pov) == 3 and len(nepov) == 4:
#         if sum(nepov) / 4 < pov[0]:
#             if k > mx:
#                 print(sum(i))

# sp = [list(map(int, i.split())) for i in open("09.txt")]
# k = 0
# # print(sp)
# for i in sp:
#     k += 1
#     if len(set(i)) == 5:
#         spsort = sorted(i)
#         if (spsort[0] + spsort[-1]) * 2 == 3 * sum(spsort[1:4]):
#             print(k)


# sp = [list(map(int, i.split())) for i in open("09.txt")]
# k = 0
# # print(sp)
# for i in sp:
#     spsort = sorted(i)
#     if (spsort[3] + spsort[4]) * 2 > 3 * sum(spsort[0:3]):
#         if len([u for u in i if u % 10 == 5]) >= 2:
#             k += 1
#
# print(k)


