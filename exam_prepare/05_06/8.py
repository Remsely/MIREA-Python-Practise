def main(x):
    x = int(x)
    r5 = x >> 32 & 2 ** 9 - 1
    r4 = x >> 27 & 2 ** 5 - 1
    r2 = x >> 9 & 2 ** 10 - 1
    r1 = x & 2 ** 9 - 1
    return r1, r2, r4, r5


print(main('1995843470136'))