# a = '012345'
# sh = 0
# for q in a:
#     for w in a:
#         for e in a:
#             for r in a:
#                 for t in a:
#                     if q == '0':
#                         continue
#                     s = q + w + e + r + t
#                     if s.count('5') >= 2 and (s.count('1') + s.count('3')) <= 3:
#                         sh += 1
# print(sh)
#
from itertools import product
a = '0123456789ABCDE'
sh = 0
for q,w,e,r in product(a, repeat=4):
    s = q + w + e + r
    if s.count('8') == 1 and ((q != w) and (w != e) and (e != r)) and q != '0':
        sh += 1
print(sh)