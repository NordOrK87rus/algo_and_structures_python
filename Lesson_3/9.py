# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

N = 5

m = []
for i in range(N):
    m.append([randint(-10, 10) for _ in range(N)])

print("Исходная матрица:")
for i in range(N):
    for j in range(N):
        print("%4d" % m[i][j], end='')
    print()

mins = []

for i in range(N):
    mins.append(m[i][0])
    for j in range(1, N):
        if mins[i] > m[j][i]:
            mins[i] = m[j][i]

mmax = mins[0]
for v in mins[1:]:
    if v > mmax:
        mmax = v

print(f"\nСписок минимальных значений колонок: ", mins)

print(f"\nМаксимальное значение из минимальных значений колонок матрицы: {mmax}")



