# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def multupl(d):
    for i in range(2, 10):
        if d % i:
            return False
    return True


cnt = 0
for i in range(2, 100):
    m = multupl(i)
    cnt += int(m)
    print(f"{i} - {m}", end=' ')

print(f"\n{cnt}")
