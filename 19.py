def f(s,m):
    if s <= 505: return m%2==0
    if m==0: return 0
    h = [f(s-3,m-1), f(s//5,m-1)]
    return any(h) if (m-1)%2==0 else any(h)
print('19)' , max([s for s in range(506,30000) if f(s, 2)]))

for i in range(506,30000):
    print(i)

def f(s,m):
    if s <= 505: return m%2==0
    if m==0: return 0
    h = [f(s-3,m-1), f(s//5,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('20)' , [s for s in range(506,10000) if not f(s, 1) and f(s, 3)])
print('21)' , [s for s in range(506,10000) if not f(s, 2) and f(s, 4)])