from pygame import*
init() # настройка на ваше железо и драйвера
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Первое приложение")

#координаты героя
x, y = 100, 345
step = 10
#изображение героя и фона
img1 = transform.scale(image.load('Герои/kitty/shutterstock_1220361823-[Converted]-2.png'), (100, 150))
background = transform.scale(image.load("Фоны/city_1.png"), (win_width, win_height))
def move():
    global x
    keys = key.get_pressed()
    if keys[K_LEFT] and x > 5:
        x -= step
    if keys[K_RIGHT] and x < 620:
        x += step
run = True
while run:
    #цикл срабатывает каждую 0.1 секунду time.delay(50)
    # #перебираем все события,которые могли произойти
    for e in event.get():
        #размещаем картинки на окне приложения
        if e.type == QUIT:
            run = False
    move()
    window.blit(background,(0,0))
    window.blit(img1, (x,y))
    #обновление окна
    time.delay(50)
    display.update()
    
quit()

"""     if e.type == KEYDOWN:
            #проверяем, а что за кнопка нажата
            if e.key == K_LEFT:
                x -= step
            if e.key == K_RIGHT:
                x += step"""