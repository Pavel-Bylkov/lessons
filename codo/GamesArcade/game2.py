import arcade
from arcade.color import *

WIDTH = 800
HEIGHT = 600
TITLE = "Game 2"

HERO_IMG = ":resources:images/alien/alienBlue_front.png"


class MyGame(arcade.Window):
    def __init__(self, width, height, window_title):
        super().__init__(width, height, window_title)
        # задаем фон окна
        arcade.set_background_color(color=DARK_GREEN)

        self.sprite = arcade.Sprite(filename=HERO_IMG, scale=0.5,
                                    center_x=width//2, center_y=height//2)
        self.speed = 5
        self.center_x = width//2
        self.center_y = height//2
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def on_draw(self):
        """Здесь мы очищаем экран и отрисовываем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        # старт рисования
        # arcade.start_render()
        self.clear()
        self.sprite.draw()
        arcade.draw_text(text="Text", start_x=10, start_y=20, color=WHITE, font_size=20)

    def on_update(self, delta_time: float):
        """Здесь мы обновляем параметры и перемещаем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        if self.move_left:
            self.center_x -= self.speed
        if self.move_right:
            self.center_x += self.speed
        if self.move_up:
            self.center_y += self.speed
        if self.move_down:
            self.center_y -= self.speed
        self.sprite.set_position(self.center_x, self.center_y)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.move_left = True
        if key == arcade.key.RIGHT:
            self.move_right = True
        if key == arcade.key.UP:
            self.move_up = True
        if key == arcade.key.DOWN:
            self.move_down = True

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.move_left = False
        if key == arcade.key.RIGHT:
            self.move_right = False
        if key == arcade.key.UP:
            self.move_up = False
        if key == arcade.key.DOWN:
            self.move_down = False


game = MyGame(width=WIDTH, height=HEIGHT, window_title=TITLE)
game.run()
