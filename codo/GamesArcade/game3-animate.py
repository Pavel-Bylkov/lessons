import random
import time

import arcade
from arcade.color import *

WIDTH = 800
HEIGHT = 600
TITLE = "Game 3"


COIN_IMG = ":resources:images/items/coinGold.png"
CURSOR = ":resources:images/pinball/pool_cue_ball.png"
SOUND = ":resources:sounds/jump5.wav"


class Hero(arcade.AnimatedWalkingSprite):
    def __init__(self, scale, center_x, center_y, speed):
        super().__init__(scale=scale,
                         center_x=center_x, center_y=center_y)
        self.speed = speed
        self.stand_right_textures.append(arcade.load_texture("animations/r1.png"))
        self.stand_left_textures.append(arcade.load_texture("animations/l1.png"))
        for i in range(1, 6):
            self.walk_left_textures.append(arcade.load_texture(f"animations/l{i}.png"))
            self.walk_right_textures.append(arcade.load_texture(f"animations/r{i}.png"))



class Button(arcade.SpriteSolidColor):
    def __init__(self, center_x, center_y, width, height, color, text, text_color):
        super(Button, self).__init__(width, height, color)
        self.text = text
        self.text_color = text_color
        self.center_x = center_x
        self.center_y = center_y
        self.sound = arcade.Sound(SOUND)   # подготавливаем звук

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super(Button, self).draw()
        arcade.draw_text(text=self.text,
                         start_x=self.center_x - len(self.text)//2 * self.height//2,
                         start_y=self.center_y - self.height//4,
                         color=self.text_color,
                         font_size=self.height//2)

    def on_click(self):
        self.sound.play(volume=0.5)


class Coin(arcade.Sprite):
    def reset_pos(self):
        self.center_x = random.randint(20, WIDTH - 20)
        self.center_y = random.randint(20, HEIGHT - 20)


class Cursor(arcade.Sprite):
    def __init__(self):
        super().__init__(filename=CURSOR, scale=0.2,
                         center_x=WIDTH//2, center_y=HEIGHT//2)

    def get_pos(self):
        return (self.center_x, self.center_y)


class MyGame(arcade.Window):
    def __init__(self, width, height, window_title):
        super().__init__(width, height, window_title)
        # задаем фон окна
        arcade.set_background_color(color=DARK_GREEN)

        self.sprite = Hero(scale=2,
                           center_x=width//2, center_y=height//2, speed=5)

        self.coins_list = arcade.SpriteList()
        self.big_coins_list = arcade.SpriteList()

        self.coins = [self.coins_list, self.big_coins_list]
        self.score = 0
        self.timer = 10
        self.last_time = time.time()  # запоминаем текущее значение времени

        self.cursor = Cursor()

        self.button = Button(center_x=WIDTH//2, center_y=HEIGHT//2,
                             width=150, height=30,
                             color=RED, text="START", text_color=BLACK)
        self.button_list = arcade.SpriteList()
        self.button_list.append(self.button)
        self.start()

    def start(self):
        self.sprite.center_x = WIDTH//2
        self.sprite.center_y = HEIGHT//2
        for i in range(20):
            coin = Coin(filename=COIN_IMG, scale=0.4,
                                 center_x=random.randint(20, WIDTH - 20),
                                 center_y=random.randint(20, HEIGHT - 20))
            self.coins_list.append(coin)
        for i in range(20):
            coin = arcade.Sprite(filename=COIN_IMG, scale=0.8,
                                 center_x=random.randint(20, WIDTH - 20),
                                 center_y=random.randint(20, HEIGHT - 20))
            self.big_coins_list.append(coin)
        self.score = 0
        self.timer = 10
        self.last_time = time.time()

    def on_draw(self):
        """Здесь мы очищаем экран и отрисовываем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        # старт рисования
        # arcade.start_render()
        self.clear()
        self.coins_list.draw()
        self.big_coins_list.draw()
        self.sprite.draw()
        arcade.draw_text(text=f"Score {self.score}", start_x=10, start_y=20,
                         color=WHITE, font_size=20)
        arcade.draw_text(text=f"Time {self.timer}", start_x=10, start_y=HEIGHT - 20,
                         color=WHITE, font_size=20)

        if len(self.coins_list) == 0 and len(self.big_coins_list) == 0:
            self.button.draw()

        self.cursor.draw()

    def on_update(self, delta_time: float):
        """Здесь мы обновляем параметры и перемещаем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""

        if self.timer > 0:
            self.sprite.update()
            self.sprite.update_animation()

        collisions = arcade.check_for_collision_with_lists(self.sprite, self.coins)
        for coin in collisions:
            coin.remove_from_sprite_lists()
            self.score += 1


    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.sprite.change_x = - self.sprite.speed
        if key == arcade.key.RIGHT:
            self.sprite.change_x = self.sprite.speed
        if key == arcade.key.UP:
            self.sprite.change_y = self.sprite.speed
        if key == arcade.key.DOWN:
            self.sprite.change_y = - self.sprite.speed

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.sprite.change_x = 0
        if key == arcade.key.RIGHT:
            self.sprite.change_x = 0
        if key == arcade.key.UP:
            self.sprite.change_y = 0
        if key == arcade.key.DOWN:
            self.sprite.change_y = 0

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.set_position(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            collide = arcade.get_sprites_at_point(self.cursor.get_pos(), self.button_list)
            for button in collide:
                button.on_click()
                self.start()


game = MyGame(width=WIDTH, height=HEIGHT, window_title=TITLE)
game.run()

"""self.player = arcade.AnimatedWalkingSprite() -создаем объект класса,
в котором реализованны параметры для хранения картинок движения спрайта

self.player_list.update() -обновление всех элементов, которые переданы в список
self.player_list.update_animation() -обновление параметров класса
AnimatedWalkingSprite()

arcade.load_texture(#текстура) -загружает текстуру из вашего диска в проект

self.player = arcade.AnimatedTimeBasedSprite() -объект класса, в котором
реализованы функции хранения кадров спрайта

frame = arcade.AnimationKeyframe(#id, #длительность показа слайда, #текстура)
-объект класса, который используется для хранения элементов в объекте
arcade.AnimatedTimeBasedSprite()

self.frames = [] -список для хранения кадров спрайта
self._points-присваивание объекту списка точек для коллизии

#текстура.hit_box_points -получение размеров изображения по 4 точкам
(верние -левая, правая, нижние -левая, правая)"""
