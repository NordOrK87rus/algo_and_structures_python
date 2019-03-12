"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""
start_sym_code = 32
last_sym_code = 127

print("--- С помощью рекурсии ---")


def get_line(s, res="", c=0):
    if c == 10 or s == last_sym_code+1:
        return s, f"{res}"
    else:
        return get_line(s + 1, f"{res} {chr(s)}", c + 1)


s = start_sym_code
while s <= 127:
    s, y = get_line(s)
    print(y)
    z = 0

print("\n--- С помощью цикла ---")
c = 0
s = start_sym_code
while s <= last_sym_code:
    if c < 10:
        print(f"{chr(s)}", end=" ")
        c += 1
    else:
        c = 1
        print(f"\n{chr(s)}", end=" ")
    s += 1
