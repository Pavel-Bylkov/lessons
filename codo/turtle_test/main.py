from turtle import *

shape('turtle')


def figura(n, lenth):
    pendown()
    color('red', 'yellow')
    begin_fill()
    for i in range(n):
        forward(lenth)
        left(360 // n)
    end_fill()
    penup()


figura(3, 100)
goto(0, -100)
figura(4, 100)
goto(200, 0)
figura(5, 50)

exitonclick()
done()
