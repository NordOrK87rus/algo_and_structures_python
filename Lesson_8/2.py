"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
s = input("Введите строку: ")


def get_subs(string):
    if len(string) == 1:
        return {hash(string)}
    else:
        res = {hash(string)} | get_subs(string[1:])
        return res


result = set()
s_len = len(s)
for i in range(s_len):
    result.add(hash(s[i]))
    result |= get_subs(s[:s_len - i])

print(f"Количество различных подстрок в строке: {len(result ^ {hash(s)})}")
