import math


def ex3_1(x):
    x = x + x
    x = x + x
    return x + x + x


def ex3_2(x):
    x = x + x
    x = x + x
    x = x + x
    return x + x


def ex3_3(x):
    a = x
    x = x + x
    x = x + x
    x = x + x
    a = a - x
    return x - a


def ex3_4(b, n, a):
    result = 0
    for i in range(1, n + 1):
        for j in range(1, b + 1):
            result += (34 * i + 41) ** 4 - 93 * (j + 79 + j ** 3) ** 5

    mul = 1
    for i in range(1, a + 1):
        summ = 0
        for j in range(1, b + 1):
            summ += 22 * (j - 8) ** 5 - i ** 4
        mul *= summ

    return result - mul


def ex3_5(x):
    if x < 13:
        return x ** 5
    if 13 <= x < 87:
        return x ** 7 - 1 - (math.floor(x)) ** 3 / 54
    if x >= 87:
        return math.ceil(x) ** 3


def ex3_6(n):
    if n == 0:
        return 3
    return math.sin(ex3_6(n - 1)) - (1 / 16) * ex3_6(n - 1) ** 3


print(ex3_4(2, 2, 6))
print(ex3_5(14))
print(ex3_6(8))
