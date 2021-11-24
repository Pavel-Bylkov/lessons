# pip install replit-play

import play

from config import param_lines

# todo

# fon = play.new_image(
#         image='labirint.jpeg',
#         x=0, y=0, angle=0, size=60,
#         transparency=100
#     )

# todo скорректировать координаты линий и длины - убрать хвосты
lines = [play.new_line(color='blue', **args, thickness=8, x1=None, y1=None)
         for args in param_lines]

box = play.new_box(
        color='black', x=-240, y=240,
        width=30, height=30,
        border_color="light blue",
        border_width=1
    )

key = play.new_image(
        image='key.png',
        x=0, y=110, angle=0, size=2,
        transparency=100
    )


@play.repeat_forever
async def move_box():

    old_x, old_y = box.x, box.y
    if play.key_is_pressed('up', 'w'):
        box.y += 5   # y = y + 15   y += 15
    elif play.key_is_pressed('down', 's'):
        box.y -= 5

    if play.key_is_pressed('right', 'd'):
        box.x += 5
    elif play.key_is_pressed('left', 'a'):
        box.x -= 5

    if box.x != old_x or box.y != old_y:
        for line in lines:
            if box.is_touching(line):
                box.x, box.y = old_x, old_y

    await play.timer(seconds=0.001)


# @play.mouse.when_clicked
# def do():
#     box.go_to(play.mouse)

play.start_program()
