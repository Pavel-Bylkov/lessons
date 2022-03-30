import arcade
from arcade.color import BLACK, GREEN, WHITE, YELLOW, DARK_GREEN

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
# заканчиваем рисование
arcade.finish_render()


arcade.run()