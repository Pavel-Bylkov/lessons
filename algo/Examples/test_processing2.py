from processing import *

from random import randint
from math import pi, sin, cos

width = 400
height = 400

nodesTotal = 100 # число узлов
nodesDelay = 22 # время появления нового узла
curDelay = 0
elMinSize = 5 # размер итогового кружка
elMaxSize = 30

stripesMin = 8 # минимальное число полос от узла
stripesMax = 10 # максимальное число полос от узла
stripesLength = 100 # средняя длина полосы
stripesLengthD = 1 # разброс длин полосы

exponent = 1 #кривизна линий

# узел:
class Node():
    def __init__(self, ):
        self.x_center = randint(left, right)                        # - центральная точка
        self.y_center = randint(top, bottom)
        self.step = randint(1, 10)                                   # - величина шага на пути линии
        self.last_size = randint(elMinSize, elMaxSize)                  
        self.lasting = randint(int(nodesDelay/1), nodesDelay)       # - время застывания итоговых фигур
#        self.delay = nodesDelay                                     # - сколько кадров осталось до генерации следующего узла

class Stripe():
    def __init__(self, number, node, angle, distance, delta2=0):
        self.node_number = number
        self.start_x = node.x_center
        self.start_y = node.y_center
        self.cur_x = node.x_center
        self.cur_y = node.y_center

        self.step = node.step                    # - величина шага на пути линии
        self.delta = (node.last_size - 1) * self.step / 100  # изменение размера за шаг
        self.lasting = node.lasting              # - время застывания итоговых фигур

        a = angle 
        if delta2 > 0:
            a += randint(-1 * delta2, delta2) * pi / 180 
        self.dist_x =  distance * cos(a)
        self.dist_y =  distance * sin(a)

        self.pct = 0
        self.size = 1

    def nextStep(self):
        self.pct = self.step + self.pct
        if self.pct < 100:
            self.cur_x = self.start_x + (self.pct * self.dist_x / 100) 
            self.cur_y = self.start_y + (pow(self.pct/100, exponent) * self.dist_y) 
            self.size = self.size + self.delta
        else:
            self.lasting = self.lasting - 1

nodes = [] # список узлов
stripes = [] # список полос
blankNodes = [] # здесь храним неиспользованные номера

def newNode(i):
    nd = Node()
    # append or insert to list of nodes

    if i < len(nodes):
        nodes.pop(i)
        nodes.insert(i, nd)
    else:
        nodes.append(nd)
    # creating stripes
    points = randint(stripesMin, stripesMax)
    distance = randint(stripesLength - stripesLengthD, stripesLength + stripesLengthD) 
    angle = 2 * pi / points 
    a = 0
    while a < 2 * pi:
        #create stripe
        l = Stripe(i, nd, a, distance, delta2=10)
        #append to list
        stripes.append(l)
        a += angle

def clearStripes():
    for l in stripes:
        if l.lasting <= 0:
            stripes.remove(l)

def createBlankNodes():
    for i in range(nodesTotal):
        blankNodes.append(True)

def clearBlankNodes():
    for i in range(nodesTotal):
        blankNodes[i] = True

def resetBlankNodes():
    for i in range(nodesTotal):
        if blankNodes[i] :
            newNode(i)


def setup():
    global width, height, left, right, top, bottom

    size(480, 480)
    frameRate(48)
    noStroke()
    background(155)
    
    width = environment.width
    height = environment.height
    left = int(1*width/8)
    right = int(7*width/8)
    top = int(1*height/8)
    bottom = int(7*height/8)

    createBlankNodes()

    #for debug:
    # print(nodes[0].x_center, ' ', nodes[0].y_center)
    # for a in range(7):
    #     sss = ''
    #     for l in stripes:
    #         l.nextStep()
    #         sss = sss + ' ' + str(l.size)
    #     print(sss)

def draw():
    global curDelay

    if curDelay <= 0 and len(nodes) < nodesTotal:
        newNode(len(nodes))
        curDelay = nodesDelay

    curDelay -= 1

    fill(0, 5) 
    rect(0, 0, width, height) 

    clearBlankNodes()
    
    clearStripes()
    # pushMatrix()

    for l in stripes:
        # если номер узла еще задействован, его не надо удалять:
        if blankNodes[l.node_number]:
            blankNodes[l.node_number] = False
        # делаем шаг, потом отрисовка:
        l.nextStep()
        fill(255)
        pushMatrix()
        if l.pct < 100:
            rotate((100-l.pct) / 500.0)
        ellipse(l.cur_x, l.cur_y, l.size, l.size)
        popMatrix()

    if len(nodes) >= nodesTotal:
        resetBlankNodes()

run()