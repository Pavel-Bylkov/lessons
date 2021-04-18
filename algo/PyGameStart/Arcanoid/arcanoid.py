import pygame as pg
pg.init()  # рекомендация от разработчиков Pygame запускать настройку конфигурации библиотеки
WIN_X, WIN_Y = 1420, 900
FPS = 40
BLUE = (200, 255, 255)
RED = (210, 55, 0)

class GameSprite(pg.sprite.Sprite):
    def __init__(self, img, x, y, size_x, size_y, speed) -> None:
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(img), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
class Brick(pg.sprite.Sprite):
    def __init__(self, x, y, size_x, size_y) -> None:
        super().__init__()
        self.image = pg.Surface((size_x, size_y))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
                brick = Brick(x=10 + j * 100, y=10 + i * 50, size_x=96, size_y=46)
                self.bricks.add(brick)
    def start_init(self):
        self.finish = False
        self.run = True
    def draw(self):
        self.window.fill(BLUE)
        # вызываем метод window.blit(self.image, (self.rect.x, self.rect.y)) у всех спрайтов группы
        self.bricks.draw(self.window)  
    def game_loop(self):
        self.start_init()
        while self.run:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.run = False
            if not self.finish:
                self.draw()
                pg.display.update()
            self.clock.tick(FPS)
game = Game()
game.game_loop()