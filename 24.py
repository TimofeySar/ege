f = open('24.txt').readline().split('K9')
mm = 0
for i in range(len(f) - 151):
    s = 0
    for j in range(i, i+151):

        s += len(f[j])
        # if len(f[j])>=1:
        #     if j == i + 149:
        #             if f[j][-1] == 'D':
        #                 s -=1


    mm = max(s, mm)
print(mm + 151*2)
