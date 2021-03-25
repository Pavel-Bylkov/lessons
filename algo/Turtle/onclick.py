from turtle import *
from random import randint
from time import sleep

def start(t, color, width, left):
    t.color(color)
    t.width(width)
    t.left(left)
w = 200
h = 200
t1 = Turtle(shape='turtle')
start(t1, color='blue', width=5, left=0)
 
t2 = Turtle(shape='turtle')
start(t2, color='green', width=5, left=120)
 
t3 = Turtle(shape='turtle')
start(t3, color='red', width=5, left=-120)

def random_pos(t):
    t.penup()
    t.goto(randint(-100,100),randint(-100,100))
    t.pendown()
    t.left(randint(0, 180))

def catch1(x, y):
    random_pos(t1)
def catch2(x, y):
    random_pos(t2)
def catch3(x, y):
    random_pos(t3)

t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

def is_inside(t):
    return abs(t.xcor()) < w and abs(t.ycor()) < h

while is_inside(t1) and is_inside(t2) and is_inside(t3):
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1)

t1.clear()
t2.clear()
t3.clear()

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
 
exitonclick()
