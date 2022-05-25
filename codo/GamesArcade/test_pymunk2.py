import arcade
import pymunk
from arcade.color import *

import random
import timeit
import math
from math import degrees

WIDTH = 800
HEIGHT = 600
IMG_COIN = "les2img/coin.png"

START_POS = (698, 500)

space = pymunk.Space()
space.gravity = (0, -1000)

class Coin(arcade.Sprite):
    def __init__(self, filename, scale, position):
        super().__init__(filename, scale=scale,
                         center_x=position[0], center_y=position[1])
        self.mass = 1
        self.radius = 25
        circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, circle_moment)
        self.body.position = position
        circle_shape = pymunk.Circle(self.body, self.radius)
        circle_shape.elasticity = 0.2
        circle_shape.friction = 1
        space.add(self.body, circle_shape)

    def update(self):
        self.angle = degrees(self.body.angle)
        self.set_position(self.body.position.x, self.body.position.y)
        if self.body.position.y < -100:
            self.remove_from_sprite_lists()
            space.remove(self.body)
            print(len(space.bodies))

class Line:
    def __init__(self, start_x, start_y, end_x, end_y, color, line_width):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color
        self.line_width = line_width
        shape = pymunk.Segment(space.static_body, (start_x, start_y),
                               (end_x, end_y), radius=line_width)
        shape.elasticity = 0.8
        shape.friction = 1
        space.add(shape)

    def draw(self):
        arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y,
                         self.color, self.line_width)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(AMAZON)

        self.coin_list = arcade.SpriteList()
        self.line_list = [
            Line(400, 300, 700, 320, RED, 2),
            Line(-200, 200, 500, 150, RED, 2)]

        self.sprite = arcade.Sprite(IMG_COIN, scale=0.1,
                                    center_x=START_POS[0],
                                    center_y=START_POS[1])

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.sprite.draw()
        for line in self.line_list:
            line.draw()

    def on_update(self, delta_time):
        space.step(delta_time)
        self.coin_list.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.coin_list.append(Coin(IMG_COIN, 0.1, START_POS))
            print(len(space.bodies))

def main():
    game = MyGame(WIDTH, HEIGHT, "pymunk")
    game.run()

main()