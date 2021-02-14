from pygame import*
init() # настройка на ваше железо и драйвера
window = display.set_mode((700, 500))
display.set_caption("Первое приложение")

#координаты героя
x = 100
y = 395
step = 10
#изображение героя и фона
img1 = transform.scale(image.load('Герои/kitty/shutterstock_1220361823-[Converted]-2.png'), (100, 100))
background = transform.scale(image.load("Фоны/city_1.png"), (700,500))
run = True
while run:
    #цикл срабатывает каждую 0.1 секунду time.delay(50)
    # #перебираем все события,которые могли произойти
    for e in event.get():
        #размещаем картинки на окне приложения
        if e.type == QUIT:
            run = False
    keys = key.get_pressed()
    if keys[K_LEFT]:
        x -= step
        if x < 5:
            x += step 
    if keys[K_RIGHT]:
        x += step
        if x > 620:
            x -= step 
    window.blit(background,(0,0))
    window.blit(img1, (x,y))
    #обновление окна
    display.update()
    time.delay(50)
quit()

"""     if e.type == KEYDOWN:
            #проверяем, а что за кнопка нажата
            if e.key == K_LEFT:
                x -= step
            if e.key == K_RIGHT:
                x += step"""