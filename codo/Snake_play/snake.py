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

play.start_program()
