def check(A):
    # Проверяем значения m и n в разумном диапазоне
    for m in range(100):
        for n in range(100):
            # Само логическое выражение из условия
            f = (2 * m + 3 * n > 40) or ((m < A) and (n <= A))

            # Если хотя бы раз выражение ложно, это А нам не подходит
            if not f:
                return False
    return True


# Перебираем А и выводим первое подошедшее
for A in range(100):
    if check(A):
        print(A)
        break