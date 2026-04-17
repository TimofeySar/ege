# a = "КОСУФ"
# sh = 0
# ssh = 1
# for q in a:
#     for w in a:
#         for e in a:
#             for r in a:
#                 for t in a:
#                     sh += 1
#                     s = q+w+e+r+t
#                     if s.count('Ф') == 0 and s.count('У') == 2:
#                         ssh = sh
# print(ssh)

from itertools import product

# Определяем алфавит (обязательно в алфавитном порядке!)
letters = sorted('МАРТ') # ['А', 'М', 'Р', 'Т']

# Генерируем все возможные комбинации по 4 буквы
# repeat=4, так как слова 4-буквенные
words = list(product(letters, repeat=4))

# Находим 250-е слово (индекс 249, так как нумерация в Python с 0)
target_word = words[249]

# Склеиваем кортеж букв в строку и выводим
print("".join(target_word))