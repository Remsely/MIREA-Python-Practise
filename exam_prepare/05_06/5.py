import math


def main(y, x, z):
    result = 0
    n = len(x)
    for i in range(n):
        result += 98 * math.log2(
            38 * z[n - math.ceil((i + 1) / 3)] ** 2
            - 7 * x[i] ** 3
            - y[n - math.ceil((i + 1) / 2)]
        ) ** 6
    return result * 34


print(main([0.88, -0.28, -0.33, -0.69, -1.0, -0.71, 0.83, 0.28],
[-0.43, -0.36, -0.51, -0.13, -0.17, -0.46, -0.14, 0.69],
[0.49, 0.91, -0.59, -0.46, 0.3, -0.21, -0.7, -0.21]))
