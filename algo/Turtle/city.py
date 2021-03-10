from turtle import *
screensize(canvwidth=700, canvheight=500)
def move_to(x, y):
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
    move_to(x, y)
    walls(size)
    for i in range(1, 4):
        move_to(x + size // 5, y + size * 3 // 4 * i)
        window(size // 4)
        move_to(x + size // 5 * 3, y + size * 3 // 4 * i)
        window(size // 4)

def land():
    pensize(300)
    color('green')
    move_to(-600, -200)
    fd(1200)
    pensize(120)
    color('grey')
    move_to(-600, -360)
    fd(1200)

def sky():
    pensize(800)
    color('light blue')
    move_to(-600, 250)
    fd(1200)

def sun(x, y):
    pensize(3)
    color('orange')
    move_to(x, y)
    begin_fill()
    for i in range(19):
        left(100)
        forward(120)
    end_fill()
    move_to(x, y + 60)
    pensize(10)
    color('orange', 'gold')
    begin_fill()
    circle(60)
    end_fill()
    right(100)


