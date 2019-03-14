"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

array_len = 6
a = [randint(0, 100) for _ in range(array_len)]

max_v, min_v, min_i, max_i = None, None, None, None

for i in range(len(a)):
    if a[i] > max_v:
        max_i = i
    elif a[i] < min_v:
        min_i = i

print(f"Исходный массив: {a}")
#  Варинт 1
s = a[min_i+1]
for i in range(min_i+1, max_i):
    s += i
print(f"Вариант 1: Сумма = {s}")


