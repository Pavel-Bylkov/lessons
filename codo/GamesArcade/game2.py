import arcade
from arcade.color import *

WIDTH = 800
HEIGHT = 600
TITLE = "Game 2"


class MyGame(arcade.Window):
    def __init__(self, width, height, window_title):
        super().__init__(width, height, window_title)
        # задаем фон окна
        arcade.set_background_color(color=DARK_GREEN)

    def on_draw(self):
        # старт рисования
        # arcade.start_render()
        self.clear()

game = MyGame(width=WIDTH, height=HEIGHT, window_title=TITLE)
game.run()