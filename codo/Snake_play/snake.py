import play

play.set_backdrop("light blue")
# Создание спрайтов
# todo суперяблоко добавить

# print(play.screen.width, play.screen.height)  # получаем размер экрана
y_top = 290
y_bottom = -290
x_right = 390
x_left = -390
score = 0

apple = play.new_box(color='red', x=play.random_number(-19, 19) * 20,
                     y=play.random_number(-14, 14) * 20, width=19, height=19,
                     border_color="yellow", border_width=1)

had = play.new_box(color='green', x=0, y=0, width=19, height=19,
                   border_color="light blue", border_width=1)

display = play.new_text(words=('%.03d' % score), x=350, y=270, angle=0,
                        font=None, font_size=50, color='black', transparency=100)

borders = [
    play.new_line(color='green', x=x_left, y=y_top, length=780, angle=0,
                  thickness=3, x1=None, y1=None),
    play.new_line(color='green', x=x_left, y=y_bottom, length=780, angle=0,
                  thickness=3, x1=None, y1=None),
    play.new_line(color='green', x=x_left, y=y_bottom, length=580, angle=90,
                  thickness=3, x1=None, y1=None),
    play.new_line(color='green', x=x_right, y=y_bottom, length=580, angle=90,
                  thickness=3, x1=None, y1=None)
]

# Переменные конфиг
speed = 0.5  #


# Функция движения
@play.repeat_forever
async def move_snake():

    had.move(20)

    if had.x > 390 or had.x < -390 or had.y > 290 or had.y < -290:
        had.move(-20)

    await play.timer(seconds=speed)


@play.repeat_forever
async def eat_control():
    global score

    if had.is_touching(apple):
        score += 1
        display.words = ('%.03d' % score)
        apple.hide()
        x = play.random_number(-19, 19) * 20
        y = play.random_number(-14, 14) * 20
        flag = True
        while flag:
            flag = False
            for sprite in play.all_sprites:
                if sprite.x == x and sprite.y == y:
                    x = play.random_number(-19, 19) * 20
                    y = play.random_number(-14, 14) * 20
                    flag = True
        apple.x = x
        apple.y = y
        apple.show()

    await play.timer(seconds=speed//4)


@play.repeat_forever
async def keys_control():
    if play.key_is_pressed('up', 'w'):
        had.angle = 90
    if play.key_is_pressed('down', 's'):
        had.angle = -90
    if play.key_is_pressed('right', 'd'):
        had.angle = 0
    if play.key_is_pressed('left', 'a'):
        had.angle = 180
    await play.timer(seconds=0.001)

play.start_program()
