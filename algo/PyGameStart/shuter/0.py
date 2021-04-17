from pygame import *

#фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()

# нам нужны такие картинки:
img_back = "galaxy.jpg" # фон игры

init()
# Создаем окошко
win_width, win_height = 1200, 800
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
clock = time.Clock()
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    #time.delay(50)
    clock.tick(30)
