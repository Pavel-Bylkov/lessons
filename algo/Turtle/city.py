from turtle import *


def _move_to(x, y):
    penup()
    goto(x, y)
    pendown()


def house(x, y, size):
    def window(size):
        color('yellow', 'light blue')
        begin_fill()
        for i in range(4):
            fd(size)
            right(90)
        end_fill()
        fd(size//2)
        right(90)
        fd(size)
        right(90)
        fd(size // 2)
        right(90)
        fd(size // 2)
        right(90)
        fd(size)
    def walls(size):
        color('grey', 'orange')
        begin_fill()
        for i in range(2):
            fd(size)
            left(90)
            fd(size*3)
            left(90)
        end_fill()
    pensize(2)
    _move_to(x, y)
    walls(size)
    for i in range(1, 4):
        _move_to(x + size // 5, y + size * 3 // 4 * i)
        window(size // 4)
        _move_to(x + size // 5 * 3, y + size * 3 // 4 * i)
        window(size // 4)


def land():
    pensize(300)
    color('green')
    _move_to(-1000, -200)
    fd(2000)
    pensize(120)
    color('grey')
    _move_to(-1000, -360)
    fd(2000)


def sky():
    pensize(800)
    color('light blue')
    _move_to(-800, 250)
    fd(1600)


def sun(x, y):
    pensize(3)
    color('orange')
    _move_to(x, y)
    begin_fill()
    for i in range(19):
        left(100)
        forward(120)
    end_fill()
    _move_to(x, y + 60)
    pensize(10)
    color('orange', 'gold')
    begin_fill()
    circle(60)
    end_fill()
    right(100)


