import math


def f(y):
    if y < -17:
        return (1 - y - y ** 2 / 67) ** 2 - 26 * y ** 2 - 1
    if -17 <= y < 33:
        return (y ** 2 / 95) ** 5 / 97 - y ** 6 / 91
    if 33 <= y < 52:
        return math.ceil(y - 0.01 - y ** 2) / 68 + 53 * y ** 3 + math.tan(
            y / 4 + 59 * y ** 2) ** 7 / 87
    if 52 <= y < 84:
        return 58 * y ** 2
    if y >= 84:
        return y ** 4 / 94 - abs(y ** 2 / 53 - 1 - 66 * y)


def main(y):
    return f(y)
