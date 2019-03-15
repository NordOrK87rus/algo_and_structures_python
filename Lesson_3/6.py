"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

array_len = 6
a = [randint(0, 100) for _ in range(array_len)]
max_v, min_v, min_i, max_i = a[0], a[0], 0, 0

for i in range(len(a)):
    if a[i] > max_v:
        max_i = i
        max_v = a[i]
    elif a[i] < min_v:
        min_i = i
        min_v = a[i]

if min_i > max_i:
    min_i, max_i = max_i, min_i

print(f"Исходный массив: {a}")

#  Варинт 1
s1 = 0
for i in range(min_i+1, max_i):
    s1 += a[i]
print(f"Вариант 1: Сумма = {s1}")


# Вариант 2
s2 = sum(a[min_i+1:max_i])
print(f"Вариант 2: Сумма = {s2}")
