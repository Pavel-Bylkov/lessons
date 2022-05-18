import random
import time

import arcade
from arcade.color import *
from arcade.experimental.lights import Light, LightLayer

# ToDo

WIDTH = 800
HEIGHT = 600

VIEW_MARGIN = 200  # ширина рамки после которого начнет двигаться экран
TITLE = "Game 4"


COIN_IMG = "timeanim/coinanim.png"
COIN_IMG2 = ":resources:images/items/coinGold.png"
CURSOR = ":resources:images/pinball/pool_cue_ball.png"
SOUND = ":resources:sounds/jump5.wav"
MUSIC = ":resources:music/funkyrobot.mp3"


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


class Coin(arcade.AnimatedTimeBasedSprite):
    def __init__(self, scale, center_x, center_y):
        super(Coin, self).__init__(scale=scale, center_x=center_x, center_y=center_y)
        for row in range(2):
            for col in range(3):
                texture = arcade.load_texture(COIN_IMG,
                                              x=col * 220, y=row * 230,
                                              width=220, height=230)
                frame = arcade.AnimationKeyframe(tile_id=1, duration=80, texture=texture)
                self.frames.append(frame)
                self._points = texture.hit_box_points  # для отслеживания столкновений

    def reset_pos(self):
        self.center_x = random.randint(20, WIDTH - 20)
        self.center_y = random.randint(20, HEIGHT - 20)


class Cursor(arcade.Sprite):
    def __init__(self):
        super().__init__(filename=CURSOR, scale=0.2,
                         center_x=WIDTH//2, center_y=HEIGHT//2)

    def get_pos(self):
        return (self.center_x, self.center_y)


class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.sprite = Hero(scale=2,
                           center_x=self.window.width//2,
                           center_y=self.window.height//2, speed=5)

        self.coins_list = arcade.SpriteList()
        self.big_coins_list = arcade.SpriteList()

        self.coins = [self.coins_list, self.big_coins_list]
        self.score = 0
        self.timer = 10
        self.last_time = time.time()  # запоминаем текущее значение времени

        # подготавливаем звуки
        self.music = arcade.Sound(MUSIC)  # фоновая музыка
        self.sound_effect = arcade.Sound(SOUND)  # звук сбора монет
        self.player = None  # понадобиться для управления музыкой
        self.start()

        # для управления координатами экрана - перемещения
        self.view_left = 0
        self.view_bottom = 0

        # работаем со световыми слоями
        self.light_layer = LightLayer(WIDTH, HEIGHT)
        self.light = Light(self.sprite.center_x, self.sprite.center_y,
                           radius=100.0, color=(255, 255, 255), mode='hard')
        self.light_layer.add(self.light)

    def on_show(self):
        # задаем фон окна
        arcade.set_background_color(color=DARK_GREEN)

    def start(self):
        self.view_left = 0
        self.view_bottom = 0
        self.sprite.center_x = WIDTH//2
        self.sprite.center_y = HEIGHT//2
        self.sprite.change_x = 0
        self.sprite.change_y = 0
        for i in range(20):
            coin = Coin(scale=0.2,
                        center_x=random.randint(20, WIDTH - 20),
                        center_y=random.randint(20, HEIGHT - 20))
            self.coins_list.append(coin)
        for i in range(20):
            coin = arcade.Sprite(filename=COIN_IMG2, scale=0.5,
                                 center_x=random.randint(20, WIDTH - 20),
                                 center_y=random.randint(20, HEIGHT - 20))
            self.big_coins_list.append(coin)
        self.score = 0
        self.timer = 10
        self.last_time = time.time()
        # останавливаем звук если он уже был запущен
        if self.player is not None:
            self.music.stop(self.player)
        self.player = self.music.play(volume=0.5, loop=True)  # loop - повторение

    def on_draw(self):
        """Здесь мы очищаем экран и отрисовываем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        # старт рисования
        # arcade.start_render()
        self.clear()
        with self.light_layer:
            self.coins_list.draw()
            self.big_coins_list.draw()
            self.sprite.draw()

        self.light_layer.draw(ambient_color=(50, 50, 50))

        arcade.draw_text(text=f"Score {self.score}",
                         start_x=10+self.view_left, start_y=20+self.view_bottom,
                         color=WHITE, font_size=20)
        arcade.draw_text(text=f"Time {self.timer}",
                         start_x=10+self.view_left, start_y=HEIGHT - 20+self.view_bottom,
                         color=WHITE, font_size=20)

    def on_update(self, delta_time: float):
        """Здесь мы обновляем параметры и перемещаем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""

        self.coins_list.update_animation()
        if self.timer > 0:
            self.sprite.update()
            self.sprite.update_animation()  # обязательно для анимации

        collisions = arcade.check_for_collision_with_lists(self.sprite, self.coins)
        for coin in collisions:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.sound_effect.play(volume=0.5)

        if len(self.coins_list) == 0 and len(self.big_coins_list) == 0:
            restart = Restart(self)
            self.window.show_view(restart)

        self.light.position = self.sprite.position

        self.view_point()

    def view_point(self):
        #создание границ для персонажа и камеры
        left_boundary = self.view_left + VIEW_MARGIN
        if self.sprite.left < left_boundary:
            self.view_left -= left_boundary - self.sprite.left

        right_boundary = self.view_left + self.window.width - VIEW_MARGIN
        if self.sprite.right > right_boundary:
            self.view_left += self.sprite.right - right_boundary

        bottom_boundary = self.view_bottom + VIEW_MARGIN
        if self.sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.sprite.bottom

        top_boundary = self.view_bottom + self.window.height - VIEW_MARGIN
        if self.sprite.top > top_boundary:
            self.view_bottom += self.sprite.top - top_boundary

        arcade.set_viewport(self.view_left,
                            self.view_left + self.window.width,
                            self.view_bottom,
                            self.view_bottom + self.window.height)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.sprite.change_x = - self.sprite.speed
        if key == arcade.key.RIGHT:
            self.sprite.change_x = self.sprite.speed
        if key == arcade.key.UP:
            self.sprite.change_y = self.sprite.speed
        if key == arcade.key.DOWN:
            self.sprite.change_y = - self.sprite.speed
        if key == arcade.key.P:
            pause = Pause(self)
            self.window.show_view(pause)
        if key == arcade.key.SPACE:
            if self.light in self.light_layer:
                self.light_layer.remove(self.light)
            else:
                self.light_layer.add(self.light)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.sprite.change_x = 0
        if key == arcade.key.RIGHT:
            self.sprite.change_x = 0
        if key == arcade.key.UP:
            self.sprite.change_y = 0
        if key == arcade.key.DOWN:
            self.sprite.change_y = 0


class MainMenu(arcade.View):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.text = "For start game press any key"

    def on_show(self):
        arcade.set_background_color(color=DARK_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text(text=self.text,
                         start_x=self.window.width //2 - len(self.text) // 2 * 25,
                         start_y=self.window.height //2 - 20,
                         color=GREEN,
                         font_size=40)

    def on_key_press(self, symbol: int, modifiers: int):
        game = MyGame()
        self.window.show_view(game)


class Pause(arcade.View):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def on_show(self):
        # задаем фон окна
        arcade.set_background_color(color=DARK_GREEN)
        self.game.player.pause()

    def on_draw(self):
        """Здесь мы очищаем экран и отрисовываем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        self.clear()
        self.game.on_draw()
        arcade.draw_rectangle_filled(center_x=self.window.width // 2+self.game.view_left,
                                     center_y=self.window.height // 2+self.game.view_bottom,
                                     width=300,
                                     height=200, color=ASH_GREY)
        arcade.draw_text(text="PAUSE",
                         start_x=self.window.width // 2 - 100+self.game.view_left,
                         start_y=self.window.height // 2 - 20+self.game.view_bottom,
                         color=GREEN,
                         font_size=40)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.P:
            self.game.player.play()
            self.window.show_view(self.game)


class Restart(arcade.View):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.button = Button(center_x=self.window.width // 2,
                             center_y=self.window.height // 2,
                             width=150, height=30,
                             color=RED, text="START", text_color=BLACK)
        self.button_list = arcade.SpriteList()
        self.button_list.append(self.button)
        self.cursor = Cursor()

    def on_draw(self):
        """Здесь мы очищаем экран и отрисовываем спрайты.
        Этот метод вызывается автоматически с частотой 60 кадров в секунду"""
        self.clear()
        self.game.on_draw()

        self.button.draw()
        self.cursor.draw()

    def on_update(self, delta_time: float):
        self.button.set_position(self.window.width // 2+self.game.view_left,
                             self.window.height // 2+self.game.view_bottom)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor.set_position(x+ self.game.view_left, y+ self.game.view_bottom)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            collide = arcade.get_sprites_at_point((x+ self.game.view_left,
                                                   y+ self.game.view_bottom), self.button_list)
            for button in collide:
                button.on_click()
                self.game.start()
                self.window.show_view(self.game)


main_window = arcade.Window(width=WIDTH, height=HEIGHT, title=TITLE)

menu = MainMenu()
main_window.show_view(menu)

main_window.run()

"""
from arcade.experimental.lights import Light,LightLayer
-импорт класса для создания лучей и светового слоя

self.light_layer = LightLayer(WIDTH,HEIGHT)
-создание светового слоя

self.light = Light(x,y,radius,color,mode)
-создание луча света

with self.light_layer:
    -отрисовка бекграунда вместо со световым слоем
    (всё что должно быть освещено световым слоем должно быть внутри оператора with)
    self.background_list.draw()
    self.player_sprite_list.draw()

self.light_layer.draw(ambient_color=default_color)
-отрисовка светового слоя с общим светом на весь слой

arcade.set_viewport(
    self.view_left,self.view_left + self.width,
    self.view_bottom,
    self.view_bottom + self.height)
-установка координат которые будут охватывать текущее окно

"""
