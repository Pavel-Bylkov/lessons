import pygame as pg
from time import time

from pygame.constants import FINGERMOTION
pg.init()  # рекомендация от разработчиков Pygame запускать настройку конфигурации библиотеки
WIN_X, WIN_Y = 1420, 900
FPS = 50
BLUE = (200, 255, 255)
RED = (210, 55, 0)
GREEN = (50, 150, 50)
DARK_BLUE = (30, 55, 155)
img_ball = "ball.png"

class Ball(pg.sprite.Sprite):
    def __init__(self, img, x, y, size_x, size_y, speed) -> None:
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(img), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = speed
        self.dy = speed
        self.change_direction("up-down")
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def change_direction(self, direction):
        #если мяч достигает границ экрана, меняем направление его движения
        if  direction == "up-down":
            self.dy *= -1
        if direction == "left-right":
            self.dx *= -1
    def update(self):
        #придаём постоянное ускорение мячу по x и y
        self.rect.x += self.dx
        self.rect.y += self.dy

class BallCircle(pg.sprite.Sprite):
    def __init__(self, x, y, radius, speed, color) -> None:
        super().__init__()
        self.cicrle_radius = radius
        self.circle_center = [x, y]
        self.dx = speed
        self.dy = speed
        self.color = color

    def draw(self, window):
        self.rect = pg.draw.circle(window, self.color, self.circle_center, self.cicrle_radius, 10)

    def change_direction(self):
        #если мяч достигает границ экрана, меняем направление его движения
        if  self.circle_center[1] < self.cicrle_radius:
            self.dy *= -1
        if self.circle_center[0] > WIN_X - self.cicrle_radius or self.circle_center[0] < self.cicrle_radius:
            self.dx *= -1
    def update(self):
        #придаём постоянное ускорение мячу по x и y
        self.circle_center[0] += self.dx
        self.circle_center[1] += self.dy
        self.change_direction()

class Brick(pg.sprite.Sprite):
    def __init__(self, x, y, size_x, size_y, color, speed=0) -> None:
        super().__init__()
        self.image = pg.Surface((size_x, size_y))
        self.image.fill(color)
        self.color = color
        self.border_color = DARK_BLUE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
       
class Platform(Brick):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.x < WIN_X - self.rect.width:
            self.rect.x += self.speed
    def reset(self, window):
        # Заливка
        pg.draw.rect(window, self.color, self.rect)
        #обводка существующего прямоугольника
        pg.draw.rect(window, self.border_color, self.rect, 10)
        
class Game():
    def __init__(self) -> None:
        self.window = self.create_window()
        self.clock = pg.time.Clock()  # создаем таймер
        self.font150 = pg.font.SysFont('verdana', 150)
        self.font40 = pg.font.SysFont('verdana', 40)
        self.last_time = time()
        self.create_sprites()
    def create_window(self):
        return pg.display.set_mode((WIN_X, WIN_Y))
    def create_sprites(self):
        self.bricks = pg.sprite.Group()
        self.platform = Platform(x=WIN_X//2, y=WIN_Y - 50, size_x=150, size_y=30, color=GREEN, speed=10)
        self.ball = Ball(img_ball ,x=WIN_X//2+60, y=WIN_Y - 100, size_x=40, size_y=40, speed=5)
        self.walls = pg.sprite.Group()
        self.top = Brick(x=0, y=0, size_x=WIN_X, size_y=5, color=DARK_BLUE)
        self.left = Brick(x=0, y=0, size_x=5, size_y=WIN_Y, color=DARK_BLUE)
        self.right = Brick(x=WIN_X - 5, y=0, size_x=5, size_y=WIN_Y, color=DARK_BLUE)
        self.bottom = Brick(x=0, y=WIN_Y - 5, size_x=WIN_X, size_y=5, color=DARK_BLUE)
        self.walls.add(
            self.top,
            self.left,
            self.right,
            self.bottom
        )
        self.win = self.font150.render("YOU WIN", True, GREEN)
        self.lose = self.font150.render("YOU LOSE", True, RED)

    def start_init(self):
        self.score = 0
        self.finish = False
        self.run = True
        for i in range(6):  # количество рядов кирпичей
            for j in range(14):  # количество кирпичей в ряду
                brick = Brick(x=10 + j * 100, y=10 + i * 50, size_x=96, size_y=46, color=RED)
                self.bricks.add(brick)
        self.ball.rect.x, self.ball.rect.y = WIN_X//2+60, WIN_Y - 100
        self.platform.rect.x, self.platform.rect.y = WIN_X//2, WIN_Y - 50

    def draw(self):
        self.window.fill(BLUE)
        # вызываем метод window.blit(self.image, (self.rect.x, self.rect.y)) у всех спрайтов группы
        self.bricks.draw(self.window)
        self.platform.reset(self.window)
        self.ball.reset(self.window)
        self.walls.draw(self.window)
        if self.finish:
             self.window.blit(self.final, (WIN_X//2 - 300, WIN_Y//2 - 90))

    def update(self):
        if not self.finish:
            self.platform.update()
            #если мяч коснулся ракетки, меняем направление движения
            self.ball.update()
        if self.ball.rect.colliderect(self.platform.rect):
            self.ball.change_direction("up-down")
        collides = pg.sprite.spritecollide(self.ball, self.bricks, dokill=True)
        if collides:
            self.ball.change_direction("up-down")
            self.score += len(collides)
        if self.ball.rect.colliderect(self.top.rect):
            self.ball.change_direction("up-down")
        if self.ball.rect.colliderect(self.left.rect) or self.ball.rect.colliderect(self.right.rect):
            self.ball.change_direction("left-right")
        if not self.finish and self.ball.rect.colliderect(self.bottom.rect):
            self.finish = True
            self.final = self.lose
            self.last_time = time()
        if not self.finish and len(self.bricks) == 0:
            self.finish = True
            self.final = self.win
            self.last_time = time()

    def game_loop(self):
        self.start_init()
        while self.run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.run = False
            self.update()
            self.draw()
            if self.finish and time() - self.last_time > 3:
                self.bricks.empty()
                self.start_init()
            pg.display.update()
            self.clock.tick(FPS)
game = Game()
game.game_loop()