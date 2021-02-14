from processing import *

theta = 0.0
length = 60

def setup():
   frameRate(20)
   size(300,300)

def draw():
   global theta
   background(0)
   stroke(255)
   pushMatrix()
   a = mouse.x / environment.width * 90
   theta = radians(a)
   translate(environment.width/2, environment.height)
   line(0,0,0,-1*length)
   translate(0, -1*length)
   branch(length)
   popMatrix()

def branch(h):
   newh = h * 2 / 3
   if newh > 3:
       pushMatrix()
       rotate(theta)
       line(0,0,0,-1*newh)
       translate(0,-1*newh)
       branch(newh)
       popMatrix()
       pushMatrix()
       rotate(-1*theta)
       line(0,0,0,-1*newh)
       translate(0,-1*newh)
       branch(newh)
       popMatrix()

def keyPressed():
   global length
   if keyboard.keyCode == UP:
       length = length + 1
   elif keyboard.keyCode == DOWN:
       length = length - 1

run()