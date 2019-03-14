# 4.	Определить, какое число в массиве встречается чаще всего.

a = input("Введите элементы массива разделённые пробелами: ")
a = [int(i) for i in a.split()]

# Вариант 1
f = None
f_max = 0

for i in a:
    ic = a.count(i)
    if ic > f_max:
        f_max = ic
        f = i

print(f"Число {f} встречается чаще всего ({f_max} раз(а))")

# Вариант 2
f = a[0]
f_max = 1
arr_len = len(a)
for i in range(arr_len-1):
    frq = 1
    for j in range(i+1, arr_len):
        if a[i] == a[j]:
            frq += 1
    if frq > f_max:
        f_max = frq
        f = a[i]

print(f"Число {f} встречается чаще всего ({f_max} раз(а))")

