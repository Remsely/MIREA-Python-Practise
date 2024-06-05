import math


def main(O):
    P = {math.floor(o / 5) + o % 3 for o in O if not (-48 <= o <= 53)}
    _O = {abs(o) + 4 * o for o in O if 65 >= o > -15}
    Y = {math.ceil(p / 8) + abs(p) for p in P if p < 89}
    D = {math.ceil(o / 7) for o in _O if o > 40}
    k = sum(d for d in D) - sum(d * y for d in D for y in Y)
    return k


print(main({-32, -63, -25, -84, -17, 50, -72, 88, -36, -34}))
