f = open('24_23762.txt').readline()
mas = f.split('Y')
mm = 0

for j in range(0, len(mas) - 81):
    sim = 0
    sh = 0
    for i in range(j, j + 81):
        sh += mas[i].count('2025')
        sim += len(mas[i])
    if sh >= 90:
        mm = max(sim, mm)
print(mm + 80)