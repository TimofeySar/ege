f = open('24_21421.txt').readline()
for i in "QWERTYUIOPSDFGHJKLZXCVNM":
    f = f.replace(i, ' ')
a = f.split(' ')
mm = 0
for i in a:
    if i != ' ':
        q = int(i, 12)
        if q % 2 == 0:
            if len(i) > mm:
                if i[0] == '0':
                    mm = len(i) - 1
                else:
                    mm = len(i)
print(mm)