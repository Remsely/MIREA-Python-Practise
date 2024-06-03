from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='>'):
    pattern = FMT[ty]
    size = calcsize(order + pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_g(buf, offs):
    g1, offs = parse(buf, offs, 'uint8')
    g2, offs = parse(buf, offs, 'float')
    g3, offs = parse(buf, offs, 'float')
    return dict(G1=g1, G2=g2, G3=g3), offs


def parse_f(buf, offs):
    f1, offs = parse(buf, offs, 'uint32')
    f2, offs = parse(buf, offs, 'uint64')
    f3, offs = parse(buf, offs, 'float')
    f4, offs = parse(buf, offs, 'double')
    f5, offs = parse(buf, offs, 'uint8')
    f6, offs = parse(buf, offs, 'int16')
    return dict(F1=f1, F2=f2, F3=f3, F4=f4, F5=f5, F6=f6), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'int16')
    e2size, offs = parse(buf, offs, 'uint16')
    e2offs, offs = parse(buf, offs, 'uint32')
    e2 = []
    for _ in range(e2size):
        val, e2offs = parse(buf, e2offs, 'uint32')
        e2.append(val)
    e3, offs = parse(buf, offs, 'int64')
    return dict(E1=e1, E2=e2, E3=e3), offs


def parse_d(buf, offs):
    d1, offs = parse_e(buf, offs)
    d2, offs = parse(buf, offs, 'int16')
    return dict(D1=d1, D2=d2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int16')
    c2, offs = parse(buf, offs, 'uint8')
    c3, offs = parse(buf, offs, 'uint8')
    return dict(C1=c1, C2=c2, C3=c3), offs


def parse_b(buf, offs):
    b1, offs = parse_c(buf, offs)
    b2, offs = parse(buf, offs, 'int16')
    b3, offs = parse(buf, offs, 'double')
    b4, offs = parse(buf, offs, 'double')
    b5, offs = parse(buf, offs, 'int8')
    b6, offs = parse(buf, offs, 'float')
    b7, offs = parse(buf, offs, 'uint8')
    b8size, offs = parse(buf, offs, 'uint16')
    b8offs, offs = parse(buf, offs, 'uint32')
    b8 = []
    for _ in range(b8size):
        val, b8offs = parse_d(buf, b8offs)
        b8.append(val)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8), offs


def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2, offs = parse(buf, offs, 'uint8')
    a3, offs = parse(buf, offs, 'uint16')
    a4offs, offs = parse(buf, offs, 'uint32')
    a4, _ = parse_f(buf, a4offs)
    a5 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'char')
        a5.append(val.decode('ascii'))
    a6, offs = parse(buf, offs, 'double')
    a7 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'int8')
        a7.append(val)
    a8, offs = parse_g(buf, offs)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=''.join(a5), A6=a6, A7=a7,
                A8=a8), offs


def main(stream):
    res, _ = parse_a(stream, 5)
    return res


data = (b'AZDG\x82I\x7f\xc6\xed9\x1b?\xe6\x8c\xe1\xbfNM\xec?\xd2\xe0v\xe1\xd6\x1fl\xdc'
        b'?\x19n\xb1l\x00\x02\x00\x00\x00]\x15\xc5Z\x00\x00\x00\x81yuirwiu?\xd8\xb7'
        b'G\xce!\x05lq\xaa~P\xbf\x19z[?o\xf3\x92m\xde\xae\x90=2\xe0\x9b\xdc\x88\xd7'
        b'\x03\xd5\x0eH$\xab\xf1e]V\xcd\x00\x02\x00\x00\x00I\xe1\x16\x10'
        b'\x1d\x00\x13\x9b\x9c\xbe\xfe\xaa~\x00\x03\x00\x00\x00QG\x8d7x\xd4'
        b'\x84\x8c\xc5\xa8\xab\xdd\xbb2a[\x17\xb5\xea\x8dD\xdf\x91?\x17\x18'
        b'`\xbf\xe6\xd1w\xb8\xdf\xd8\x9e\xba\xeen')

print(main(data))
