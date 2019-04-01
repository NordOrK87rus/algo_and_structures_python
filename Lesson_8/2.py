"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

# s = input("Введите строку: ")
s = "pasta"
result = set()

for i in range(len(s)):
    if i == 0:
        n = len(s) - 1
    else:
        n = len(s)

    for j in range(n, i, -1):
        # substr.add(hash(str_in[i:j]))
        result.add(s[i:j])


# <class 'set'>: {'p', 'asta', 'ta', 'st', 'sta', 's', 'a', 'ast', 'pa', 'past', 'as', 't', 'pas'} len=13
# print(f"Количество различных подстрок в строке: {len(substr)}")
