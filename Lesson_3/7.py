"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

array_len = 6
a = [randint(-10, 100) for _ in range(array_len)]
print(f"Исходный массив: {a}")

mins = []
mins.append(min(a))
a.remove(mins[0])
mins.append(min(a))

print(f"Два минимальных значения: {mins[0]} и {mins[1]}")
