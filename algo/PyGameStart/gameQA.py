import pygame

pygame.init()
mw = pygame.display.set_mode((500, 500))
back = (255, 42, 91)  #цвет фона (background)
mw.fill(back)

clock = pygame.time.Clock()
fps = 60

#цвета
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)

class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """ область: прямоугольник в нужном месте и нужного цвета """
        #запоминаем прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = color
    #установить текст
    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        font = pygame.font.Font(None, fsize)
        self.image = font.render(text, True, text_color)  
    #отрисовка прямоугольника с текстом
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  

#создание карточек
quest_card = TextArea(x=120, y=100, width=290, height=70, color=LIGHT_BLUE)
quest_card.set_text("Вопрос", fsize=75)
 
ans_card = TextArea(x=120, y=240, width=290, height=70, color=LIGHT_BLUE)
ans_card.set_text("Ответ", fsize=75)

run = True
while run:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
    
    quest_card.draw(shift_x=10,shift_y=10)
    ans_card.draw(shift_x=10,shift_y=10)

    pygame.display.update()
    clock.tick(fps)