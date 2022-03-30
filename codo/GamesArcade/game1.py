import arcade
from arcade.color import *

WIDTH = 800
HEIGHT = 600
TITLE = "Game 1"

# создаем окно
arcade.open_window(width=WIDTH, height=HEIGHT, window_title=TITLE)
# задаем фон окна
arcade.set_background_color(color=DARK_GREEN)
# старт рисования
arcade.start_render()
# рисуем линию
arcade.draw_line(start_x=50, start_y=50, end_x=750, end_y=50,
                 color=YELLOW, line_width=3)
# рисуем заполненный круг
arcade.draw_circle_filled(center_x=WIDTH//2, center_y=HEIGHT//2,
                          radius=50, color=RED, tilt_angle=0,
                          num_segments=-1)
arcade.draw_circle_filled(center_x=WIDTH//2, center_y=HEIGHT//2,
                          radius=40, color=GREEN, tilt_angle=0,
                          num_segments=5)
arcade.draw_circle_filled(center_x=WIDTH//2, center_y=HEIGHT//2,
                          radius=30, color=BLUE, tilt_angle=45,
                          num_segments=5)
# рисуем пустой круг
arcade.draw_circle_outline(center_x=150, center_y=150, radius=50,
                           color=BLACK, border_width=5, tilt_angle=0,
                           num_segments=-1)
# рисуем часть закрашенного круга
arcade.draw_arc_filled(center_x=550, center_y=150, width=50, height=50,
                       color=BLUE, start_angle=15, end_angle=190, tilt_angle=30,
                       num_segments=100)
# рисуем закрашенный прямоугольник
arcade.draw_rectangle_filled(center_x=150, center_y=500, width=100, height=50,
                             color=DARK_CORAL, tilt_angle=0)
# рисуем закрашенный треугольник
arcade.draw_triangle_filled(x1=500, y1=500, x2=550, y2=550,
                            x3=600, y3=450, color=DARK_RED)


def arca(x, y):
    arcade.draw_arc_outline(x, y - 250, 370, 150, arcade.color.GREEN, 0, 180, 300)


arca(250, 250)


def house(x, y):
    arcade.draw_rectangle_filled(x, y - 100, 200, 150, arcade.color.BROWN)
    arcade.draw_circle_filled(x - 50, y - 100, 25, arcade.color.BLUEBERRY)
    arcade.draw_circle_filled(x + 50, y - 100, 25, arcade.color.BLUEBERRY)
    arcade.draw_line(x + 100, y - 100, 150, 150, arcade.color.BROWN, 3)
    arcade.draw_triangle_filled(120, 220, 260, 300, 380, 220, arcade.color.BLACK)


house(250, 250)


def sun(x, y):
    arcade.draw_circle_filled(x, y + 20, 50, arcade.color.YELLOW)
    arcade.draw_line(x - 50, y - 100, 370, 350, arcade.color.YELLOW)
    arcade.draw_line(x + 20, y - 35, 435, 320, arcade.color.YELLOW)
    arcade.draw_line(x + 20, y + 40, 280, 350, arcade.color.YELLOW)


sun(400, 400)


# заканчиваем рисование
arcade.finish_render()

# запускаем игровой цикл
arcade.run()