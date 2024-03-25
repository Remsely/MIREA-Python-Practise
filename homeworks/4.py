import math


def main(n):
    if n == 0:
        return -0.24
    if n >= 1:
        return math.tan(main(n - 1)) / 52 - main(n - 1) ** 2
