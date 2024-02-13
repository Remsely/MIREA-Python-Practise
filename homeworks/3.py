import math


def f(a, m):
    result = 0
    for i in range(1, m + 1):
        for j in range(1, a + 1):
            result += math.cos(i) ** 2 - 55 * (
                    26 * j + 44 * j ** 2 + 23 * j ** 3)
    return result


def main(a, m):
    return f(a, m)
