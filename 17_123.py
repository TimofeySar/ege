f = open('17.txt')

data = [int(x) for x in f]

count = 0
max_sum = -1e9

for i in range(len(data) - 1):
    a = data[i]
    b = data[i + 1]

    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        count += 1
        if (a + b) > max_sum:
            max_sum = a + b

print(count, max_sum)