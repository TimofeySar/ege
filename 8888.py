from itertools import product
ss = 0
a = sorted('АПРЕЛЬ')
sh = 0
for q,w,e,r,t in product(a, repeat=5):
    sh += 1
    if sh%2 !=0:
        continue
    s = q+w+e+r+t
    if q !='Ь' and q != 'Р' and s.count('Л') >= 2:
        ss = sh
print(ss)
