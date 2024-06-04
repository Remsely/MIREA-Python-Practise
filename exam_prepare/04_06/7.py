def x0(x, left, right):
    if x[0] == 1997:
        return left
    if x[0] == 1960:
        return right


def x1(x, left, mid, right):
    if x[1] == 1985:
        return left
    if x[1] == 1986:
        return mid
    if x[1] == 1997:
        return right


def x3(x, left, mid, right):
    if x[3] == 1962:
        return left
    if x[3] == 1980:
        return mid
    if x[3] == 1973:
        return right


def main(x):
    return x0(x,
              x3(x,
                 x1(x, 0, 1, 2),
                 3,
                 4),
              x1(x,
                 5,
                 x3(x,
                    6,
                    7,
                    8),
                 x3(x,
                    9,
                    10,
                    11)))


print(main([1997, 1985, 'HTTP', 1973]))
