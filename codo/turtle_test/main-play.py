# pip install replit-play

import play

box = play.new_box(
        color='black', x=0, y=0,
        width=30, height=30,
        border_color="light blue",
        border_width=1
    )

fon = play.new_image(
        image='labirint.jpeg',
        x=0, y=0, angle=0, size=60,
        transparency=100
    )

lines = [
    # верхняя рамка
    # play.new_line(color='blue', x=-285, y=280, length=565,
    #     angle=0, thickness=5, x1=None, y1=None),
    # левая рамка
    # play.new_line(color='blue', x=-285, y=-285, length=560,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-285, y=-285, length=565,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=280, y=-280, length=560,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-160, y=220, length=60,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-285, y=150, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    play.new_line(color='blue', x=-160, y=150, length=65,
        angle=0, thickness=5, x1=None, y1=None),
]



@play.repeat_forever
async def move_box():
    if play.key_is_pressed('up', 'w'):
        box.y += 15
    if play.key_is_pressed('down', 's'):
        box.y -= 15

    if play.key_is_pressed('right', 'd'):
        box.x += 15
    if play.key_is_pressed('left', 'a'):
        box.x -= 15

    await play.timer(seconds=0.01)


# @play.mouse.when_clicked
# def do():
#     box.go_to(play.mouse)

play.start_program()
