import math
import tkinter as tk


# 1
def ex4_1(x, y):
    border = 0.1
    if border < x < 1 - border and border < y < 1 - border:
        return 0, 0, 0
    else:
        return 1, 1, 1


# 3
def ex4_3(x, y):
    radius = 0.4

    x_coor = x - 0.5
    y_coor = y - 0.5

    distance = math.sqrt(x_coor ** 2 + y_coor ** 2)

    if math.sqrt((x_coor - 0.15) ** 2 + (y_coor + 0.25) ** 2) < 0.06:
        return 0, 0, 0

    if x_coor == 0 or y - 0.5 == 0:
        if distance < radius and x_coor <= 0:
            return 1, 1, 0
        else:
            return 0, 0, 0

    tang = x_coor / y_coor

    if (distance <= radius and 1.35 >= tang >= -1.35 or distance <= radius and
            x_coor < 0):
        return 1, 1, 0
    else:
        return 0, 0, 0


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def func(x, y):
    return ex4_3(x, y)


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
