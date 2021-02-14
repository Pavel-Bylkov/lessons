from turtle import *
hideturtle()
speed(0)
count = 2
angle = 10
step = 100
i = count
while i < step:
   forward(i)
   left(angle)
   i = i + count
while i > 0:
   forward(i)
   left(angle)
   i = i - count
exitonclick()