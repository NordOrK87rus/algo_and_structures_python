"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint
from timeit import timeit

m = int(input("Введите натуральное число: "))
arr = [randint(-m, m) for _ in range(m * 2 + 1)]


def med(data):
    n = len(data)
    if n < 1:
        return None
    elif n % 2 == 1:
        return sorted(data)[n // 2]
    else:
        return sum(sorted(data)[n // 2 - 1:n // 2 + 1]) / 2.0


print(f"Исходный массив:\t{arr}")
print(f"Медиана:\t\t\t{med(arr)}")
print(f"Время обработки:\t{timeit('med(arr)', setup='from __main__ import med, arr',number=100)}")
