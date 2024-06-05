def main(input_value):
    e3 = (input_value >> 4) & 2 ** 7 - 1
    e3 <<= 9

    e1 = input_value & 2 ** 2 - 1
    e1 <<= 7

    e2 = (input_value >> 2) & 2 ** 2 - 1
    e2 <<= 5
    result = e3 | e2 | e1
    return result


print(main(29))
print(main(1257))
print(main(978))
print(main(1649))


def main2(x):
    n1 = x[0][1]
    n2 = x[1][1] << 6
    n3 = x[2][1] << 11
    n4 = x[3][1] << 19
    return hex(n1 | n2 | n3 | n4)


print(main2([('N1', 18), ('N2', 27), ('N3', 13), ('N4', 31)]))
print(main2([('N1', 0), ('N2', 24), ('N3', 20), ('N4', 56)]))
print(main2([('N1', 7), ('N2', 27), ('N3', 10), ('N4', 10)]))
print(main2([('N1', 57), ('N2', 27), ('N3', 187), ('N4', 29)]))


def main3(x):
    w1 = x & 2 ** 10 - 1
    w3 = (x >> 13) & 2 ** 7 - 1
    w4 = (x >> 20) & 2 ** 7 - 1
    w5 = (x >> 27) & 2 ** 3 - 1
    w6 = (x >> 30) & 2 ** 4 - 1
    return [('W1', hex(w1)), ('W3', hex(w3)), ('W4', hex(w4)), ('W5', hex(w5)), ('W6', hex(w6))]


print(main3(6608546738))
print(main3(11577784042))
print(main3(17026265228))
print(main3(1329407077))
