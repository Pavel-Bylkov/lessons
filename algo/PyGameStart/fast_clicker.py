import pygame
import time
pygame.init()
 
'''создаём окно программы'''
 
back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((800, 500)) #окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()
 
'''класс прямоугольник'''
 
class Area():
   def __init__(self, x=0, y=0, width=10, height=10, color=None):
       self.rect = pygame.Rect(x, y, width, height) #прямоугольник
       self.fill_color = color
 
   def color(self, new_color):
       self.fill_color = new_color
 
   def fill(self):
       pygame.draw.rect(mw, self.fill_color, self.rect)
   def outline(self, frame_color, thickness): #обводка существующего прямоугольника
       pygame.draw.rect(mw, frame_color, self.rect, thickness)    
 
   def collidepoint(self, x, y):
       return self.rect.collidepoint(x, y)       
 
'''класс надпись'''
 
class Label(Area):
   def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
       self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
 
   def draw(self, shift_x=0, shift_y=0):
       self.fill()
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
 
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
 
cards = []
num_cards = 4
 
x = 170
 
for i in range(num_cards):
   new_card = Label(x, 170, 100, 100, YELLOW)
   new_card.outline(BLUE, 10)
   new_card.set_text('CLICK', 26)
   cards.append(new_card)
   x = x + 120
 
 
#Бонус: заготовки для счётчиков времени и очков
start_time = time.time()
old_time = time.time()
 
time_text = Label(0,0,50,50,back)
time_text.set_text('Время:',40, DARK_BLUE)
time_text.draw(20, 20)
 
score_text = Label(380,0,50,50,back)
score_text.set_text('Счёт:',45, DARK_BLUE)
score_text.draw(20,20)
 
timer = Label(50,55,50,40,back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)
 
score = Label(430,55,50,40,back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)
 
wait = 0
 
from random import randint
last_click = 0
run = True
while run:
    if wait == 0:
        #переносим надпись:
        wait = 30 #столько тиков надпись будет на одном месте
        click = randint(0, num_cards - 1)
        while last_click == click:
            click = randint(0, num_cards - 1)
        last_click = click
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if i == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1
 
    #на каждом тике проверяем клик:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #обработай событие «клик по кнопке "Закрыть окно"»
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                #ищем, в какую карту попал клик
                if cards[i].collidepoint(x,y):
                    if i + 1 == click: #если на карте есть надпись - перекрашиваем в зелёный, плюс очко
                        cards[i].color(GREEN)
                    else: #иначе перекрашиваем в красный, минус очко
                        cards[i].color(RED)
    
                    cards[i].fill()
 
    pygame.display.update()
    clock.tick(40)           
