import play

from time import sleep
import sys

play.set_backdrop("light blue")
# Создание спрайтов
# todo суперяблоко добавить

# print(play.screen.width, play.screen.height)  # получаем размер экрана
y_top = 290
y_bottom = -290
x_right = 390
x_left = -390
score = 0
timer = 10


apple = play.new_box(color='red', x=play.random_number(-19, 19) * 20,
                     y=play.random_number(-14, 14) * 20, width=19, height=19,
                     border_color="yellow", border_width=1)

super_apple = play.new_box(color='yellow', x=-400, y=-300, width=19, height=19,
                           border_color="red", border_width=1)
super_apple.hide()

# Тело змейки
body = []

had = play.new_box(color='green', x=0, y=0, width=19, height=19,
                   border_color="light blue", border_width=1)


def add_to_body():
    """Добавляем в список новый кусочек тела"""
    global body

    if len(body) > 0:
        x, y = body[-1].x, body[-1].y
    else:
        x, y = had.x, had.y
    body.append(
        play.new_box(color='light green', x=x, y=y, width=19, height=19,
                     border_color="light blue", border_width=1)
    )


def body_step(x, y):
    """Передвигаем все части хвоста друг за другом"""
    global body

    for chunk in body:
        old_x, old_y = chunk.x, chunk.y
        chunk.x, chunk.y = x, y
        x, y = old_x, old_y


def has_had_bite_body():
    """Проверяем касание головой хвоста"""
    global body

    for chunk in body:
        if had.x == chunk.x and had.y == chunk.y:
            return True
    return False


def get_random_free_space():
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
    return x, y

display = play.new_text(words=('%.03d' % score), x=350, y=270, angle=0,
                        font=None, font_size=50, color='black', transparency=100)

display_timer = play.new_text(words=('%.02d' % 0), x=-350, y=270, angle=0,
                              font=None, font_size=50, color='red', transparency=100)
display_timer.hide()

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

game_over = play.new_text(words="GAME OVER", x=0, y=50, angle=0,
                          font=None, font_size=150, color='red', transparency=100)
game_over.hide()

# Переменные конфиг
speed = 0.5  #

run = True


# Функция движения
@play.repeat_forever
async def move_snake():
    global run

    if run:
        old_x, old_y = had.x, had.y
        had.move(20)
        if has_had_bite_body():
            game_over.show()
            run = False
            await play.timer(seconds=2)
            sys.exit()
        body_step(old_x, old_y)

    if had.x > 390 or had.x < -390 or had.y > 290 or had.y < -290:
        game_over.show()
        run = False
        await play.timer(seconds=2)
        sys.exit()

    await play.timer(seconds=speed)


@play.repeat_forever
async def eat_control():
    global score, speed

    if had.is_touching(apple):
        add_to_body()
        score += 1
        speed -= 0.01
        display.words = ('%.03d' % score)
        apple.hide()
        apple.x, apple.y = get_random_free_space()
        apple.show()

    if had.is_touching(super_apple):
        for _ in range(4):
            add_to_body()
        score += 4
        speed -= 0.01
        display.words = ('%.03d' % score)
        super_apple.hide()
        super_apple.x, super_apple.y = -400, -300
        display_timer.hide()

    await play.timer(seconds=speed//4)


@play.repeat_forever
async def gen_super_apple():
    """Генератор супер яблок"""
    await play.timer(seconds=10)
    super_apple.x, super_apple.y = get_random_free_space()
    super_apple.show()
    display_timer.words = ('%.02d' % timer)
    display_timer.show()
    color = "yellow"
    time = timer
    for _ in range(timer):
        await play.timer(seconds=1)
        if color == "yellow":
            display_timer.color = "red"
        else:
            display_timer.color = "yellow"
        time -= 1
        display_timer.words = ('%.02d' % time)
    super_apple.hide()
    super_apple.x, super_apple.y = -400, -300
    display_timer.hide()


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
