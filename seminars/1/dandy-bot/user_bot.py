def script(check, x, y):
    if check("level") == 1:
        if check('gold', x, y) > 0:
            return 'take'
        elif check('wall', x + 2, y):
            return 'down'
        elif check('player', x + 1, y):
            return 'pass'
        else:
            return 'right'

    if check("level") == 2:
        if check('player', x + 1, y):
            return 'pass'
        elif check('gold', x, y) > 0:
            return 'take'
        elif check('gold', x + 1, y) > 0:
            return 'right'
        elif check('gold', x - 1, y) > 0:
            return 'left'
        elif check('gold', x, y + 1) > 0:
            return 'down'
        elif check('gold', x, y - 1) > 0:
            return 'up'
        else:
            if (check('wall', x, y + 1) or check('wall', x, y - 1)) and not check('wall', x + 1, y):
                return 'right'
            else:
                return 'up'

    if check("level") == 3 or check("level") == 4 or check("level") == 5:
        used_coords = dict()
        q = [(x, y)]

        if check("gold", x, y) > 0:
            return "take"

        while len(q) > 0:
            _x, _y = q.pop(0)

            if check("gold", _x, _y) > 0:
                return used_coords[(_x, _y)]
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                __x, __y = _x + dx, _y + dy
                if (__x, __y) not in used_coords and not check("wall", __x, __y):
                    if _x == x and _y == y:
                        direction = {
                            (-1, 0): "left", (0, -1): "up", (1, 0): "right", (0, 1): "down"
                        }[(dx, dy)]
                    else:
                        direction = used_coords[(_x, _y)]
                    used_coords[(__x, __y)] = direction
                    q.append((__x, __y))

        return "pass"

    return "pass"
