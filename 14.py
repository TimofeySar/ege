f = open('26 (2).txt')
n, k = map(int, f.readline().split())
state = []
for i in range(n):
    a = int(f.readline())
    state.append(a)
models = []
for i in range(k):
    a = list(map(int, f.readline().split()))
    models.append(a)
sh = 0
maxi = 0
state.sort()
models.sort(key=lambda x: [x[1], x[0]])
for i in range(len(state)):
    for j in range(len(models)):
        if state[i] <= models[j][0]:
            sh += models[j][1]
            maxi = max(maxi, models[j][0])
            break
    print(i)

print(sh, maxi)