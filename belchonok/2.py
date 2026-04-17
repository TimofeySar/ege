def digit_sum(s):
    """Сумма цифр в 12‑ричной строке (A=10, B=11)."""
    return sum(10 if c == 'A' else 11 if c == 'B' else int(c) for c in s)


def find_longest_divisible_number(s):
    max_length = 0
    n = len(s)
    valid_digits = set('0123456789AB')

    # Перебираем все возможные концы подстрок (j)
    for j in range(1, n + 1):
        # Если последняя цифра не 0 и не 6 — пропускаем (не делится на 6)
        if s[j - 1] not in '06':
            continue

        # Находим самый длинный допустимый префикс, заканчивающийся на j
        current_sum = 0
        for i in range(j - 1, -1, -1):  # идём назад от j-1 к 0
            if s[i] not in valid_digits:
                break  # недопустимый символ — прерываем

            current_sum += 10 if s[i] == 'A' else 11 if s[i] == 'B' else int(s[i])

            # Проверяем условия:
            # 1. Сумма цифр делится на 3
            # 2. Сумма цифр ≤ 120
            # 3. Длина подстроки > текущей max_length
            if (current_sum % 6 == 0 and
                    current_sum <= 120 and
                    (j - i) > max_length):
                max_length = j - i

    return max_length


# Чтение из файла
with open('Информатика_11_9.txt', 'r', encoding='utf-8') as file:
    input_string = file.read().strip()

result = find_longest_divisible_number(input_string)
print(result)
