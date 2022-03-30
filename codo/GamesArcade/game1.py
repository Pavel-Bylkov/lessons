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

# заканчиваем рисование
arcade.finish_render()

# запускаем игровой цикл
arcade.run()