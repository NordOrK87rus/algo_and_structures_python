"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
n = int(input("Введите количество элементов: "))


# С помощью рекурсии
def sum_el(n, next_num=1.0, res=0.0):
    if n == 0:
        return res
    else:
        return sum_el(n - 1, next_num / -2, res + next_num)


print(f"Recursion: {sum_el(n)}")

# С помощью цикла
num = 1
sum_res = 0
while n > 0:
    sum_res += num
    num /= -2
    n -= 1

print(f"Loop: {sum_res}")
