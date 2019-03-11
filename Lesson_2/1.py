"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def get_operator():
    op = input("Введите арифметическую операцию: ")
    if op == '0' or op == '+' or op == '-' or op == '/' or op == '*':
        return op
    else:
        return get_operator()


while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    op = get_operator()
    if op == '0':
        break
    elif op == "+":
        print(f"{a} {op} {b} = {a+b}")
    elif op == "-":
        print(f"{a} {op} {b} = {a-b}")
    elif op == "*":
        print(f"{a} {op} {b} = {a*b}")
    elif op == "/":
        print(f"{a} {op} {b} = {a/b}")
