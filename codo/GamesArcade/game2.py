import random
import time

import arcade
from arcade.color import *

WIDTH = 800
HEIGHT = 600
TITLE = "Game 2"

HERO_IMG = ":resources:images/alien/alienBlue_front.png"
COIN_IMG = ":resources:images/items/coinGold.png"
CURSOR = ":resources:images/pinball/pool_cue_ball.png"


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

        self.sprite = Hero(filename=HERO_IMG, scale=0.5,
                           center_x=width//2, center_y=height//2, speed=5)

        self.coins_list = arcade.SpriteList()
        for i in range(20):
            coin = Coin(filename=COIN_IMG, scale=0.4,
                                 center_x=random.randint(20, width - 20),
                                 center_y=random.randint(20, height - 20))
            self.coins_list.append(coin)

        self.big_coins_list = arcade.SpriteList()
        for i in range(20):
            coin = arcade.Sprite(filename=COIN_IMG, scale=0.8,
                                 center_x=random.randint(20, width - 20),
                                 center_y=random.randint(20, height - 20))
            self.big_coins_list.append(coin)

        self.coins = [self.coins_list, self.big_coins_list]
        self.score = 0
        self.timer = 10
        self.last_time = time.time()  # запоминаем текущее значение времени

        self.cursor = Cursor()

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
        self.cursor.draw()

    def on_update(self, delta_time: float):
        """Здесь мы обновляем параметры и перемещаем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""

        if self.timer > 0:
            self.sprite.update()

        # for coin in self.coins_list:
        #     if arcade.check_for_collision(self.sprite, coin):
        #         self.coins_list.remove(coin)
        #         self.score += 1

        collisions = arcade.check_for_collision_with_list(self.sprite, self.coins_list)
        for coin in collisions:
            self.coins_list.remove(coin)
            self.score += 1

        collide_distance = arcade.get_closest_sprite(self.sprite, self.big_coins_list)
        if collide_distance is not None:
            sprite, distance = collide_distance
            # print(distance)
            if distance < 150:
                sprite.remove_from_sprite_lists()  # чтобы не перепутать списки, удаляем из всех списков

        if self.timer > 0 and time.time() - self.last_time >= 1:
            self.timer -= 1
            self.last_time = time.time()  # запоминаем текущее значение времени

        # нужно совместить центр курсора и центр спрайта-монеты
        # collide = arcade.get_sprites_at_exact_point(self.cursor.get_pos(), self.coins_list)
        # for coin in collide:
        #     coin.reset_pos()

        # нужно попасть центром курсора в любую точку спрайта-монеты
        collide = arcade.get_sprites_at_point(self.cursor.get_pos(), self.coins_list)
        for coin in collide:
            coin.reset_pos()

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

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.set_position(x, y)


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