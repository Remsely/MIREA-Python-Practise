import math


def f(z, x):
    return ((z + 26 * (1 - x ** 3) ** 7) /
            (math.floor(x ** 2 - x ** 3 - z / 35) + 25)
            + 56 * z ** 2 + 57 * x)


def main(z, x):
    return f(z, x)


print(main(0.86, 0.23))
print(main(0.81, -0.63))
print(main(-0.2, 0.33))
print(main(-0.5, 0.25))
print(main(0.6, -0.68))
