import math


def main(X):
    M = {x ** 2 for x in X if -37 <= x <= 93}
    N = {7 * x - 2 * x for x in X if x not in range(0, 78)}
    Y = {v * m for v in N for m in M if v <= m}
    E = len({(e1, e2) for e1 in M for e2 in Y}) - sum(m % 2 + math.ceil(v / 9) for m in M for v in Y)
    return E

print(main({41, -15, -46, -12, -42, 87, -8, -71, 86, -67}))