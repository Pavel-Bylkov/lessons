from pygame import*
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.speed = player_speed

    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#класс спрайта-врага    
class Enemy(GameSprite):
    pass

#класс элемента стены
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
 
       # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), 
                    (self.rect.x, self.rect.y, self.width, self.height))

init()
#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))

#создаем стены
w1 = Wall(0, 0, 250, win_width / 2 - win_width / 3, win_height / 2, 300, 10)
w2 = Wall(0, 0, 250, 410, win_height / 2 - win_height / 4, 10, 350)

#создаем спрайты
packman = Player('Герои/pacman/pac-1.png', 5, win_height - 80, 5)

#переменная, отвечающая за то, как кончилась игра
finish = False

#игровой цикл
run = True
while run:
    #цикл срабатывает каждую 0.05 секунд
    time.delay(50)
    #перебираем все события, которые могли произойти
    for e in event.get():
        #событие нажатия на кнопку “закрыть”
        if e.type == QUIT:
            run = False
    if not finish:
        #обновляем фон каждую итерацию
        window.fill((0, 0, 0))

        #рисуем стены
        w1.draw_wall()
        w2.draw_wall()
        #запускаем движения спрайтов
        packman.update()
        #обновляем их в новом местоположении при каждой итерации цикла
        packman.reset()
    #Проверка столкновения героя с врагом и стенами
    if sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2):
        finish = True
        #вычисляем отношение
        img = image.load('gameover.jpeg')
        d = img.get_width() // img.get_height()
        window.fill((0, 0, 0))
        window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

    display.update()

