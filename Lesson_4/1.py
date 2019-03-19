"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit
from cProfile import run
from functools import wraps


def memorize(func):
    @wraps(func)
    def wrapper(n, memory={}):
        r = memory.get(n, None)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return wrapper


def num_counter1(arr):
    # @memorize
    def count_n(n):
        return arr.count(n)

    n, n_max = None, 0

    for i in arr:
        ic = count_n(i)
        if ic > n_max:
            n, n_max = i, ic
    return n, n_max


def num_counter2(arr):
    # @memorize
    def count_n(n):
        cnt = 0
        for j in range(arr_len):
            cnt += 1 if a[j] == n else 0

            # if a[j] == n:
            #     cnt += 1
        return cnt

    arr_len = len(arr)
    f, f_max = None, 0

    for i in range(arr_len):
        frq = count_n(i)
        if frq > f_max:
            f, f_max = arr[i], frq
    return f, f_max


def num_counter3(arr):
    # @memorize
    def count_n(n):
        return arr.count(n)

    n,  n_max = None, 0

    for i in set(arr):
        ic = count_n(i)
        if ic > n_max:
            n, n_max = i, ic
    return n, n_max


def num_counter4(arr):
    # @memorize
    def count_n(n):
        return arr.count(n)

    res = {i: count_n(i) for i in set(arr)}

    # res = {}
    # for i in set(arr):
    #     if i not in res.keys():
    #         res[i] = count_n(i)

    mv = max(res.values())
    for k, v in res.items():
        if v == mv:
            mk = k
            break
    return mk, mv


def main():
    num_counter1(a)
    num_counter2(a)
    num_counter3(a)
    num_counter4(a)


if __name__ == "__main__":
    a = [1, 2, 3, 1, 4, 5, 6, 1, 3]

    run('main()')

    print(f"num_counter1: {timeit.timeit('num_counter1(a)', setup='from __main__ import num_counter1, a')}")
    print(f"num_counter2: {timeit.timeit('num_counter2(a)', setup='from __main__ import num_counter2, a')}")
    print(f"num_counter3: {timeit.timeit('num_counter3(a)', setup='from __main__ import num_counter3, a')}")
    print(f"num_counter4: {timeit.timeit('num_counter4(a)', setup='from __main__ import num_counter4, a')}")

"""

"""
