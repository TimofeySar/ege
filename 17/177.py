# Читаем файл
with open('17.txt') as f:
    a = list(map(int, f.readlines()))

count = 0  # счетчик подходящих пар
max_sum = 0  # максимальная сумма

# Перебираем все пары
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        # Проверяем произведение на кратность 26
        if (a[i] * a[j]) % 26 == 0:
            count += 1
            # Обновляем максимальную сумму
            max_sum = max(max_sum, a[i] + a[j])

print(count, max_sum)
