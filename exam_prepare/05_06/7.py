def x0(x, left, mid, right):
    if x[0] == 'KICAD':
        return left
    if x[0] == 'METAL':
        return mid
    if x[0] == 'J':
        return right


def x1(x, left, right):
    if x[1] == 'REBOL':
        return left
    if x[1] == 'RAGEL':
        return right


def x2(x, left, mid, right):
    if x[2] == 1983:
        return left
    if x[2] == 1981:
        return mid
    if x[2] == 2009:
        return right


def x3(x, left, mid, right):
    if x[3] == 'OOC':
        return left
    if x[3] == 'CLIPS':
        return mid
    if x[3] == 'X10':
        return right


def x4(x, left, mid, right):
    if x[4] == 1989:
        return left
    if x[4] == 2008:
        return mid
    if x[4] == 2000:
        return right


def main(x):
    return x0(x,
              x2(x,
                 x4(x,
                    0,
                    x1(x,
                       1,
                       2),
                    x1(x,
                       3,
                       4)),
                 x4(x,
                    x3(x,
                       5,
                       7,
                       7),
                    8,
                    x1(x,
                       9, 10)),
                 11),
              12,
              13)


print(main(['KICAD', 'REBOL', 1981, 'OOC', 1989]))