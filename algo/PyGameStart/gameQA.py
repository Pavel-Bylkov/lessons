import pygame
from random import randint

pygame.init()
#создание окна игры
clock = pygame.time.Clock()
back = (255, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)
#цвета
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)
class TextArea():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
      self.fill_color = color
      #возможные надписи
      self.titles = list()
 
  #добавить текст в список возможных надписей
  def add_text(self, text):
      self.titles.append(text)
 
  #установить текст
  def set_text(self, number=0, fsize=12, text_color=BLACK):
      self.text = self.titles[number]
      self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)
    
  #отрисовка прямоугольника с текстом
  def draw(self, shift_x=0, shift_y=0):
      pygame.draw.rect(mw, self.fill_color, self.rect)
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  
#создание карточек
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
quest_card.add_text('Вопрос')
quest_card.add_text('Что изучаешь в Алгоритмике?')
quest_card.add_text('На каком языке говорят во Франции?')
quest_card.add_text('Что растёт на яблоне?')
quest_card.add_text('Что падает с неба?')
quest_card.add_text('Что едят на ужин?')
quest_card.set_text(0, 75)
ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
ans_card.add_text('Ответ')
ans_card.add_text('Python')
ans_card.add_text('Французский')
ans_card.add_text('Яблоки')
ans_card.add_text('Капли дождя')
ans_card.add_text('Жаркое с грибами')
ans_card.set_text(0, 75)
ans_card2= TextArea(120, 340, 290, 70, LIGHT_BLUE)
ans_card2.add_text('Ответ')
ans_card2.add_text('C++')
ans_card2.add_text('Английский')
ans_card2.add_text('Апельсины')
ans_card2.add_text('Снег')
ans_card2.add_text('Картофель')
ans_card2.set_text(0, 75)
quest_card.draw(10,10)
ans_card.draw(10,10)
ans_card2.draw(10,10)
right = 0 
run = True
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1, len(quest_card.titles)-1)   
                quest_card.set_text(num, 25)
                ans_card.set_text(num, 25)
                ans_card2.set_text(num, 25)
                quest_card.draw(10,25)
                ans_card.draw(10, 25)
                ans_card2.draw(10, 25)
    if pygame.mouse.get_pressed()[0] and ans_card.rect.collidepoint(pygame.mouse.get_pos()):
        right += 1
        print(right)
        pygame.time.delay(500)
    if right == 5:
        run = False
    clock.tick(40)
