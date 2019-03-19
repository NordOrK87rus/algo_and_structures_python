"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
from timeit import timeit

n = int(input("вывод простых чисел до числа: "))


def wo_eratosfen(n):
    lst = [2]
    for i in range(3, n + 1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if not i % j:
                break
        else:
            lst.append(i)
    return lst


def eratosfen(n):
    a = [i for i in range(n + 1)]
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j], j = 0, j + m
        m += 1

    return  [i for i in a if i != 0]


print(f"Без Решета Эратосфена:\n{eratosfen(n)} "
      f"({timeit('wo_eratosfen(n)', setup='from __main__ import wo_eratosfen, n')})\n---\n")

print(f"---\nРешето Эратосфена: \n{eratosfen(n)} "
      f"({timeit('eratosfen(n)', setup='from __main__ import eratosfen, n')})\n---\n")
