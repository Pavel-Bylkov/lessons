import pygame as pg
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
        self.change_direction()
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def change_direction(self):
        #если мяч достигает границ экрана, меняем направление его движения
        if  self.rect.y < 0:
            self.dy *= -1
        if self.rect.x > WIN_X - self.rect.width or self.rect.x < 0:
            self.dx *= -1
    def update(self):
        #придаём постоянное ускорение мячу по x и y
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.change_direction()

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
        self.create_sprites()
    def create_window(self):
        return pg.display.set_mode((WIN_X, WIN_Y))
    def create_sprites(self):
        self.bricks = pg.sprite.Group()
        for i in range(6):  # количество рядов кирпичей
            for j in range(14):  # количество кирпичей в ряду
                brick = Brick(x=10 + j * 100, y=10 + i * 50, size_x=96, size_y=46, color=RED)
                self.bricks.add(brick)
        self.platform = Platform(x=WIN_X//2, y=WIN_Y - 50, size_x=150, size_y=30, color=GREEN, speed=10)
        self.ball = Ball(img_ball ,x=WIN_X//2+60, y=WIN_Y - 100, size_x=40, size_y=40, speed=5)
        self.ball2 = BallCircle(x=WIN_X//2+60, y=WIN_Y - 100, radius=20, speed=5, color=DARK_BLUE)
        self.ball2.draw(self.window)
    def start_init(self):
        self.finish = False
        self.run = True
    def draw(self):
        self.window.fill(BLUE)
        # вызываем метод window.blit(self.image, (self.rect.x, self.rect.y)) у всех спрайтов группы
        self.bricks.draw(self.window)
        self.platform.reset(self.window)
        self.ball.reset(self.window)
        self.ball2.draw(self.window)
    def update(self):
        self.platform.update()
        #если мяч коснулся ракетки, меняем направление движения
        self.ball.update()
        if self.ball.rect.colliderect(self.platform.rect):
            self.ball.dy *= -1
        self.ball2.update()
        if pg.sprite.collide_rect(self.ball2, self.platform):
            self.ball2.dy *= -1
    def game_loop(self):
        self.start_init()
        while self.run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.run = False
            if not self.finish:
                self.update()
                self.draw()
                pg.display.update()
            self.clock.tick(FPS)
game = Game()
game.game_loop()