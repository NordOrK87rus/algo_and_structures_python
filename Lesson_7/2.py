"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from timeit import timeit
from random import uniform


def merge_sorting(data):
    if len(data) > 1:
        c = len(data) // 2
        l, r = data[:c], data[c:]

        for side in l, r:
            merge_sorting(side)

        i, j, k, len_l, len_r = 0, 0, 0, len(l), len(r)

        while i < len_l and j < len_r:
            if l[i] < r[j]:
                data[k] = l[i]
                i += 1
            else:
                data[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            data[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            data[k] = r[j]
            j += 1
            k += 1
        return data


data_list = [uniform(0.0, 50.0) for _ in range(5)]
print(f"Исходный массив:\t\t{data_list}")
print(f"Отсортированный массив:\t{merge_sorting(data_list)}")

print(f"Время обработки:\t\t{timeit('merge_sorting(data_list)', setup='from __main__ import merge_sorting, data_list',number=100)}")
