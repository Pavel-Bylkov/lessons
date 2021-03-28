from turtle import *
from random import randint
 
tsize = 20
s_width = 200
s_height = 180
 
class Sprite(Turtle):
   def __init__(self, x, y, step=10, shape='circle', color='black'):
       Turtle.__init__(self)
       self.penup()
       self.speed(0)
       self.goto(x, y)
       self.color(color)
       self.shape(shape)
       self.step = step
       self.points = 0

class Player(Sprite):
   def move_up(self):
       self.goto(self.xcor(), self.ycor() + self.step)
   def move_down(self):
       self.goto(self.xcor(), self.ycor() - self.step)
   def move_left(self):
       self.goto(self.xcor() - self.step, self.ycor())
   def move_right(self):
       self.goto(self.xcor() + self.step, self.ycor()) 
   def is_collide(self, sprite):
       if self.distance(sprite.xcor(), sprite.ycor()) < tsize:
           return True
       return False

class Enemy(Sprite):
   def set_move(self, x_start, y_start, x_end, y_end):
       self.x_start = x_start
       self.y_start = y_start       
       self.x_end = x_end
       self.y_end = y_end
       self.goto(x_start, y_start)
       self.setheading(self.towards(x_end, y_end)) #направление
  
   def make_step(self):
       self.forward(self.step) #направление уже есть
       if self.distance(self.x_end, self.y_end) < self.step: #если расстояние меньше полушага
           self.set_move(self.x_end, self.y_end, self.x_start, self.y_start) #меняем направление
 
player = Player(x=0, y=-100, step=10, shape='circle', color='orange')

enemy1 = Enemy(x=-s_width, y=0, step=20, shape='square', color='red')
enemy1.set_move(x_start=-s_width, y_start=0, x_end=s_width, y_end=0)

enemy2 = Enemy(x=s_width, y=70, step=20, shape='square', color='red')
enemy2.set_move(x_start=s_width, y_start=70, x_end=-s_width, y_end=70)

goal = Sprite(x=0, y=120, step=20, shape='triangle', color='green')
#goal.set_move(-s_width, 120, s_width, 0)  
 
total_score = 0
 
scr = player.getscreen()
 
scr.listen()
 
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')
 
while total_score < 3:
   enemy1.make_step()
   enemy2.make_step()
   #goal.make_step()
   if player.is_collide(goal):
       total_score += 1
       player.goto(0, -100)
   if player.is_collide(enemy1) or player.is_collide(enemy2):
       goal.hideturtle()
       break
 
if total_score == 3:
   enemy1.hideturtle()
   enemy2.hideturtle()
scr.mainloop()