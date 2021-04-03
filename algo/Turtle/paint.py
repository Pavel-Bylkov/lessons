from turtle import *
def create_turtle(color, x, y):
    t = Turtle()
    t.color(color)
    t.width(5)
    t.shape('circle')
    t.pu()
    t.goto(x, y)
    return t
v = 100  # скорость черепашки
step = 15  # шаг
def create_palitre():
    global clr
    clr = ['red', 'green', 'blue', 'yellow', 'orange', 'aqua', 'pink', 'coral', 'white', 'black']
    for i in range(10):
        clr[i] = create_turtle(clr[i], -150 + i * 30, 200)
def setColor0(x,y):
    t.color('red')
def setColor1(x,y):
    t.color('green')
def setColor2(x,y):
    t.color('blue')
def setColor3(x,y):
    t.color('yellow')
def setColor4(x,y):
    t.color('orange')
def setColor5(x,y):
    t.color('aqua')
def setColor6(x,y):
    t.color('pink')
def setColor7(x,y):
    t.color('coral')
def setColor8(x,y):
    t.color('white')
def setColor9(x,y):
    t.color('black')

create_palitre()
t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(v)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def setRed():
    t.color('red')

def setGreen():
    t.color('green')

def setBlue():
    t.color('blue')

def stepUp():
    t.goto(t.xcor(), t.ycor() + step)

def stepDown():
    t.goto(t.xcor(), t.ycor() - step)

def stepLeft():
    t.goto(t.xcor() - step, t.ycor())

def stepRight():
    t.goto(t.xcor() + step, t.ycor())

def startFill():
    t.begin_fill()

def endFill():
    t.end_fill()

def screen_clear():
    t.clear()

t.ondrag(draw)

scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(setRed, 'r')
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')
scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepRight, 'Right')
scr.onkey(startFill, 'f')
scr.onkey(endFill, 'e')
scr.onkey(screen_clear, 'l')

scr.listen()

clr[0].onclick(setColor0)
clr[1].onclick(setColor1)
clr[2].onclick(setColor2)
clr[3].onclick(setColor3)
clr[4].onclick(setColor4)
clr[5].onclick(setColor5)
clr[6].onclick(setColor6)
clr[7].onclick(setColor7)
clr[8].onclick(setColor8)
clr[9].onclick(setColor9)

scr.mainloop()