import pygame

pygame.init()
pygame.display.set_caption("Вопрос-Ответ")
window = pygame.display.set_mode((500, 500)) #окно программы (main window)
back = (55, 55, 255) #цвет фона (background)
fill_color = (50, 150, 30)
text_color = (150, 50, 30)
window.fill(back)
# Создаем прямоугольник в координатах x=50 y=50 размером widht=400 height=100
rect = pygame.Rect(50, 50, 400, 100)
# Создаем изображение из текста
text_image = pygame.font.Font(None, 70).render("Тестовый текст", True, text_color)

clock = pygame.time.Clock()
run = True
while run:
    pygame.draw.rect(window, fill_color, rect)
    window.blit(text_image, (70, 80))  # копируем изображение с текстом в координаты x=70 y=80
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(40) # создает микропаузу, из расчета 40 кадров в секунду