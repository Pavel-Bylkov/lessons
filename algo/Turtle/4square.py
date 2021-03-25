from turtle import *
 
def set_atrib(turtle, color, shape, speed):
    turtle.color(color)
    turtle.shape(shape)
    turtle.speed(speed)

def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

t1 = Turtle()
set_atrib(t1, 'red', 'triangle', 10)
move_to(t1, -50, 50)

t2 = Turtle()
set_atrib(t2, 'blue', 'circle', 10)
move_to(t2, -50, -50)

t3 = Turtle()
set_atrib(t3, 'green', 'turtle', 10)
move_to(t3, 50, 50)

t4 = Turtle()
set_atrib(t4, 'orange', 'square', 10)
move_to(t4, 50, -50)
 
# Основной цикл: повторяется движение вперёд и влево:
i = 5
while i < 50:
    for t in (t1, t2, t3, t4):
        t.forward(2*i)
        t.left(90)
    i = i + 2
 
# Задерживаем картинку на экране
for t in (t1, t2, t3, t4):
    t.hideturtle()

exitonclick()
