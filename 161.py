g = [0] * 50000
for i in range(1, 10):
    g[i] = 3*i
for i in range(10, 49500):
    g[i] = g[i-2]+ 1
f = [0]*50000
for i in range(1, 49000):
    f[i] = g[i-1]
print(f[47995])