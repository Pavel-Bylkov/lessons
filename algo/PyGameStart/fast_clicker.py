import pygame
import time
from random import randint
pygame.init()
 
'''создаём окно программы'''
back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((800, 500)) #окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()
 
'''класс прямоугольник'''
class Area():
   def __init__(self, x, y, width, height, color):
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
   new_card = Label(x=x, y=170, width=100, heigh=100, color=YELLOW)
   new_card.outline(frame_color=BLUE, thickness=10)
   new_card.set_text(text='CLICK', fsize=26)
   cards.append(new_card)
   x = x + 120
 
# счётчики времени и очков
time_text = Label(x=0, y=0, width=50, heigh=50, color=back)
time_text.set_text(text='Время:',fsize=40, text_color=DARK_BLUE)
time_text.draw(shift_x=20, shift_y=20)
 
score_text = Label(x=600, y=0, width=50, heigh=50, color=back)
score_text.set_text(text='Счёт:',fsize=45, text_color=DARK_BLUE)
score_text.draw(shift_x=20, shift_y=20)
 
timer = Label(x=50, y=60, width=50, heigh=40, color=back)
timer.start_time = time.time() 
score = Label(x=650, y=60, width=50, height=40, color=back)
score.num = 0

wait = 0
last_click = 0
run = True
while run:
    if wait == 0:
        #переносим надпись:
        wait = 25 #столько тиков надпись будет на одном месте
        click = randint(0, num_cards - 1)
        while last_click == click:
            click = randint(0, num_cards - 1)
        last_click = click
        for i in range(num_cards):
            cards[i].color(new_color=YELLOW)
            if i == click:
                cards[i].draw(shift_x=10, shift_y=40)
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
                    if i == click: #если на карте есть надпись - перекрашиваем в зелёный, плюс очко
                        cards[i].color(new_color=GREEN)
                        cards[i].draw(shift_x=10, shift_y=40)
                        score.num += 1
                    else: #иначе перекрашиваем в красный, минус очко
                        cards[i].color(new_color=RED)
                        cards[i].fill()
    
    score.set_text(text=str(score.num), fsize=40, text_color=DARK_BLUE)
    score.draw(shift_x=0, shift_y=0)
    timer.set_text(text=str(int(time.time() - timer.start_time)), fsize=40, text_color=DARK_BLUE)
    timer.draw(shift_x=0, shift_y=0)
    
    pygame.display.update()
    clock.tick(40)           
