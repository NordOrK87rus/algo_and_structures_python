"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from timeit import timeit
from random import randint


def bubble_sorting(data):
    d_len = len(data)
    for i in range(d_len - 1):
        for j in range(d_len - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


data_list = [randint(-100, 100) for _ in range(10)]
print(f"Исходный массив:        {data_list}")
print(f"Отсортированный массив: {bubble_sorting(data_list)}")

# print(timeit('bubble_sorting(data_list)',
#              setup='from __main__ import bubble_sorting, data_list',
#              number=100))

