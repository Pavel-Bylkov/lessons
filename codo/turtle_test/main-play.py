# pip install replit-play

import play


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
    # play.new_line(color='blue', x=-160, y=150, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-35, y=150, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-160, y=-95, length=60,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-160, y=-220, length=60,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-285, y=25, length=125,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=30, y=25, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=210, y=25, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=95, y=90, length=125,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-225, y=90, length=125,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-100, y=215, length=195,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-160, y=-35, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-35, y=-35, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=155, y=-95, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-95, y=-95, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-220, y=-160, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-35, y=-160, length=65,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=90, y=-160, length=190,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=-95, y=-220, length=310,
    #     angle=0, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=215, y=90, length=130,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=215, y=-95, length=125,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=155, y=155, length=125,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=155, y=-30, length=125,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=90, y=90, length=125,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=90, y=-160, length=190,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=30, y=25, length=130,
    #     angle=90, thickness=5, x1=None, y1=None),
    # play.new_line(color='blue', x=30, y=-220, length=185,
    #     angle=90, thickness=5, x1=None, y1=None),
    play.new_line(color='blue', x=-35, y=-35, length=185,
        angle=90, thickness=5, x1=None, y1=None),
]

box = play.new_box(
        color='black', x=-240, y=240,
        width=30, height=30,
        border_color="light blue",
        border_width=1
    )

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
