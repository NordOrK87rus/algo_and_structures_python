#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

array_len = 10

a = [randint(0, 100) for _ in range(array_len)]

min_i, max_i = 0, 0
for i in range(len(a)):
    if a[i] > a[max_i]:
        max_i = i
    elif a[i] < a[min_i]:
        min_i = i

print(f"Исходный массив: \t{a}")
print(f"{a[max_i]} <-> {a[min_i]}")
a[max_i], a[min_i] = a[min_i], a[max_i]
print(f"Полученный массив: \t{a}")


