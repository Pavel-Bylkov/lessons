import pygame
import time
pygame.init()
 
'''создаём окно программы'''
 
back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
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
 
'''класс надпись'''
 
class Label(Area):
   def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
       self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
 
   def draw(self, shift_x=0, shift_y=0):
       self.fill()
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
 
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
 
cards = []
num_cards = 4
 
x = 70
 
for i in range(num_cards):
   new_card = Label(x, 170, 70, 100, YELLOW)
   new_card.outline(BLUE, 10)
   new_card.set_text('CLICK', 26)
   cards.append(new_card)
   x = x + 100
 
while True:
   for card in cards:
       card.draw(10, 30)
 
   pygame.display.update()
   clock.tick(40)  