from turtle import *
from time import sleep
from random import randint

SCR_WIDTH = window_width()
SCR_HEIGHT = window_height()
TURTLE_SIZE = 10
delay = 1/10
step = 20

cellsX = round(SCR_WIDTH / (2*step)) - 1
cellsY = round(SCR_HEIGHT / (2*step)) - 1
prizeX = step * randint(-1 * cellsX, cellsX)
prizeY = step * randint(-1 * cellsY, cellsY)

STARTED = False
FINISHED = False

points = 0
nextDirX = 1
nextDirY = 0

colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta']
curColor = 1
def nextColor():
    global curColor
    curColor = 0 if curColor > 5 else curColor + 1

def setNextDir(x, y):
    global nextDirX, nextDirY
    nextDirX = x
    nextDirY = y

def stopGame():
    global FINISHED
    FINISHED = True

class Text():
    def __init__(self, x=0, y=0, txtColor='black', txtFillcolor='green', text='hello', ffont='Arial', fsize=8, ftype='normal'):
        # setup:
        penup()
        hideturtle()
        speed(0)
        goto(x, y)
        # first time write just to measure:
        self.startX = xcor()
        self.startY = ycor() + 2*fsize
        write(text, move=True, align='left', font=(ffont, fsize, ftype))
        self.endX = xcor()
        self.endY = ycor() - fsize
        goto(self.endX, self.endY)
        # creating rectangle:
        fillcolor(txtFillcolor)
        begin_fill()
        goto(self.startX, self.endY)
        goto(self.startX, self.startY)
        goto(self.endX, self.startY)
        goto(self.endX, self.endY)
        end_fill()
        # writing second time (above rectangle)
        goto(self.startX, self.startY - 2*fsize)
        fillcolor(txtColor)
        write(text, move=True, align='left', font=(ffont, fsize, ftype))

    def isInside(self, x, y):
        return (x >= self.startX) and (x <= self.endX) and (y <= self.startY) and (y >= self.endY) 

class Sprite(Turtle):
    def __init__(self, shape='turtle', color='black', step=10, x=0, y=0, dirX=1, dirY=0):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
        self.dirX = dirX 
        self.dirY = dirY 

    def setDir(self, x, y):
        self.dirX = x
        self.dirY = y
    
    def makeStep(self):
        newX = self.xcor() + self.step * self.dirX
        newY = self.ycor() + self.step * self.dirY
        self.goto(newX, newY)
    
size = step / (2*TURTLE_SIZE)
if size < 1.2 and size > 0.8:
    size = 1

head = Sprite(step=step, color='dark green')

prize = Sprite(step=0, shape='circle', x=prizeX, y=prizeY)

def headUp():
    head.setheading(90)    
    setNextDir(0, 1)
def headDown():
    head.setheading(270)    
    setNextDir(0, -1)
def headLeft():
    head.setheading(180) 
    setNextDir(-1, 0)
def headRight():
    head.setheading(0)     
    setNextDir(1, 0)

start = Text(text='  press to start  ', x=-50, y=SCR_HEIGHT/4, txtColor='white', fsize=14)
def checkStartClick(x,y):
    global STARTED
    if start.isInside(x, y):
        STARTED = True
        clear()

snake = [head]
def growSnake():
    x = snake[-1].xcor()
    y = snake[-1].ycor() 
    snake.append(Sprite(step=step, shape='circle', x=x, y=y))

def addPoint():
    global points
    points += 1
    growSnake()

def changeSnake():
    x = head.xcor()
    y = head.ycor() 
    head.setDir(nextDirX, nextDirY)
    if points > 0:
        snake.insert(1, Sprite(step=step, shape='circle', x=x, y=y, color=colors[curColor]))
        nextColor()
        while len(snake) > points + 1:
            snake[-1].hideturtle()
            snake.pop(-1)
    head.makeStep()


def isTailTouching(curX, curY):
    i = 1
    while i < len(snake):
        if (  snake[i].xcor() < curX + step/2 and snake[i].xcor() > curX - step/2 and
              snake[i].ycor() < curY + step/2 and snake[i].ycor() > curY - step/2):
            return True
        i += 1
    return False

screen = getscreen()

screen.onkey(headUp,'up arrow')
screen.onkey(headDown,'down arrow')
screen.onkey(headLeft,'left arrow')
screen.onkey(headRight,'right arrow')
screen.onkey(stopGame, 'q')
# screen.onkey(addPoint, 'w')

screen.onscreenclick(checkStartClick)

screen.listen()

while not FINISHED:
    if STARTED:
        prize.color(colors[randint(0,6)])
        changeSnake()
        curX = head.xcor()
        curY = head.ycor() 
        if curX == prizeX and curY == prizeY:
            addPoint()
            prizeX = step * randint(-1 * cellsX, cellsX)
            prizeY = step * randint(-1 * cellsY, cellsY)
            prize.goto(prizeX, prizeY)
        if curX < -1* SCR_WIDTH/2 or curX > SCR_WIDTH/2 or curY < -1* SCR_HEIGHT/2 or curY > SCR_HEIGHT/2:
            stopGame()
        if points > 1 and isTailTouching(curX, curY):
            stopGame() 
        if points < 8:
            sleep(delay)