import math


def main(x, z, y):
    n = len(x)
    result = 0
    for i in range(n):
        result += 58 * math.atan(20 * x[n - math.ceil((i + 1) / 3)] ** 3 +
                                 3 * z[n - math.ceil((i + 1) / 4)] ** 2 +
                                 y[n - math.ceil((i + 1) / 4)]) ** 7
    return 91 * result


print(main([-0.19, 0.91],
[0.64, 0.22],
[0.86, 0.63]))
