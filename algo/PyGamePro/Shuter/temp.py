from pygame import *
img_back = "galaxy.jpg" # фон игры
# Создаем окошко
win_width, win_height = 800, 500
display.set_caption("Shuter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # перебираем полученные события
    for e in event.get():
        # событие нажатия на крестик окошка
        if e.type == QUIT:
            run = False
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)