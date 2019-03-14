#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

array_len = 10
a = [randint(-10, 10) for _ in range(array_len)]

m = None
for i in range(len(a)):
    if 0 > a[i] and (m is None or a[i] > a[m]):
        m = i

print(f"Исходный массив: {a}")
if m is None:
    print("В массиве нет отрицательных чисел")
else:
    print(f"Максимальный отрицательный элемент: {a[m]} индекс {m}")
