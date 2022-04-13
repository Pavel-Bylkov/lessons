import random

import arcade
from arcade.color import *

WIDTH = 800
HEIGHT = 600
TITLE = "Game 2"

HERO_IMG = ":resources:images/alien/alienBlue_front.png"
COIN_IMG = ":resources:images/items/coinGold.png"


class Hero(arcade.Sprite):
    def __init__(self, filename, scale, center_x, center_y, speed):
        super().__init__(filename=filename, scale=scale,
                         center_x=center_x, center_y=center_y)
        self.speed = speed
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def update(self):
        if self.move_left:
            self.center_x -= self.speed
        if self.move_right:
            self.center_x += self.speed
        if self.move_up:
            self.center_y += self.speed
        if self.move_down:
            self.center_y -= self.speed
        self.set_position(self.center_x, self.center_y)



class MyGame(arcade.Window):
    def __init__(self, width, height, window_title):
        super().__init__(width, height, window_title)
        # задаем фон окна
        arcade.set_background_color(color=DARK_GREEN)

        self.sprite = Hero(filename=HERO_IMG, scale=0.5,
                           center_x=width//2, center_y=height//2, speed=5)

        self.coins_list = arcade.SpriteList()
        for i in range(20):
            coin = arcade.Sprite(filename=COIN_IMG, scale=0.5,
                                 center_x=random.randint(20, width - 20),
                                 center_y=random.randint(20, height - 20))
            self.coins_list.append(coin)

    def on_draw(self):
        """Здесь мы очищаем экран и отрисовываем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        # старт рисования
        # arcade.start_render()
        self.clear()
        self.coins_list.draw()
        self.sprite.draw()
        arcade.draw_text(text="Text", start_x=10, start_y=20, color=WHITE, font_size=20)

    def on_update(self, delta_time: float):
        """Здесь мы обновляем параметры и перемещаем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        self.sprite.update()
        for coin in self.coins_list:
            if arcade.check_for_collision(self.sprite, coin):
                self.coins_list.remove(coin)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.sprite.move_left = True
        if key == arcade.key.RIGHT:
            self.sprite.move_right = True
        if key == arcade.key.UP:
            self.sprite.move_up = True
        if key == arcade.key.DOWN:
            self.sprite.move_down = True
        if key == arcade.key.SPACE:
            for coin in self.coins_list:
                coin.set_position(center_x=random.randint(20, self.width - 20),
                                  center_y=random.randint(20, self.height - 20))

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.sprite.move_left = False
        if key == arcade.key.RIGHT:
            self.sprite.move_right = False
        if key == arcade.key.UP:
            self.sprite.move_up = False
        if key == arcade.key.DOWN:
            self.sprite.move_down = False


game = MyGame(width=WIDTH, height=HEIGHT, window_title=TITLE)
game.run()


"""
arcade.check_for_collision(#спрайт1, #спрайт2)
-возвращает True или False в зависимости от того, было столкновение 
или нет

arcade.check_for_collision_with_list(#основной спрайт,#список (arcade.SpriteList())
-возвращает список объектов с которыми произошла коллизия(столкновение)

arcade.check_for_collision_with_lists(#основной спрайт,
#список из списков, которые содержат спрайты)
-возвращает список объектов с которыми пересекся основной спрайт

sprite,distance = arcade.get_closest_sprite(#основной спрайт,
#список из спрайтов(arcade.SpriteList())
-возвращает два параметра ближайший спрайт и расстояние до него

if len(self.coin_list) == 0: -условие, когда все спрайты исчезли
    return None

arcade.get_sprites_at_exact_point(#точка, с которой будет искаться коллизия, 
#список спрайтов) 
-возвращает список объектов которые свои центром перескли указанную точку

arcade.get_sprites_at_point(#точка, с которой будет искаться коллизия, 
#список спрайтов) 
-возвращает список объектов которые перескли указанную точку

arcade.draw_text(#надпись с переменными или без,
#Координата икс,игрек, цвет,размер шрифта) 
-выводит надпись на экран
"""