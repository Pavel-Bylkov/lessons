import random
from math import degrees
import pymunk
import arcade
from arcade.color import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pymunk Pegboard Example"
IMG_BALL = ":resources:images/items/gold_1.png"
IMG_PEG = ":resources:images/pinball/bumper.png"

space = pymunk.Space()
space.gravity = (0.0, -900.0)

class Peg(arcade.Sprite):
    def __init__(self, filename, center_x, center_y):
        super().__init__(filename,
                         center_x=center_x, center_y=center_y)
        self.radius = 22
        self.width = self.radius * 2
        self.height = self.radius * 2
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = center_x, center_y
        circle_shape = pymunk.Circle(self.body, self.radius, pymunk.Vec2d(0, 0))
        circle_shape.friction = 0.3
        space.add(self.body, circle_shape)

class Ball(arcade.Sprite):
    def __init__(self, filename, center_x, center_y):
        super().__init__(filename,
                         center_x=center_x, center_y=center_y)
        self.mass = 0.5
        self.radius = 15
        self.width = self.radius * 2
        self.height = self.radius * 2
        circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius, (0, 0))
        self.body = pymunk.Body(self.mass, circle_moment)
        self.body.position = center_x, center_y
        circle_shape = pymunk.Circle(self.body, self.radius, pymunk.Vec2d(0, 0))
        circle_shape.friction = 0.3
        space.add(self.body, circle_shape)

    def update(self):
        self.angle = degrees(self.body.angle)
        self.set_position(self.body.position.x, self.body.position.y)
        if self.body.position.y < -100:
            self.remove_from_sprite_lists()
            space.remove(self.body)

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
        shape.friction = 10
        space.add(shape)

    def draw(self):
        arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y,
                         self.color, self.line_width)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.peg_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        arcade.set_background_color(AMAZON)

        self.static_lines = [
            Line(0, 10, SCREEN_WIDTH, 10, WHITE, 2),
            Line(SCREEN_WIDTH - 50, 10, SCREEN_WIDTH, 30, WHITE, 2),
            Line(50, 10, 0, 30, WHITE, 2)
        ]

        self.ticks_to_next_ball = 10

        separation = 150
        for row in range(6):
            for column in range(6):
                x = column * separation + (separation // 2 * (row % 2))
                y = row * separation + separation // 2
                self.peg_list.append(Peg(IMG_PEG, x, y))

    def on_draw(self):
        self.clear()

        self.peg_list.draw()
        self.ball_list.draw()

        for line in self.static_lines:
            line.draw()

    def on_update(self, delta_time):
        self.ticks_to_next_ball -= 1
        if self.ticks_to_next_ball <= 0:
            self.ticks_to_next_ball = 20
            x = random.randint(0, SCREEN_WIDTH)
            y = SCREEN_HEIGHT
            self.ball_list.append(Ball(IMG_BALL, x, y))

        space.step(delta_time)
        self.ball_list.update()

def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

main()