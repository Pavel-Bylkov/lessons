import play

# Создание спрайтов
had = play.new_box(color='green', x=0, y=0,
        width=20, height=20,
        border_color="light blue", border_width=1)

# Переменные конфиг
speed = 0.5  #

# Функция движения
@play.repeat_forever
async def move_snake():

    had.move(20)

    await play.timer(seconds=speed)

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

    await play.timer(seconds=0.01)

play.start_program()
