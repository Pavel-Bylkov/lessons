from pygame import*
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (60, 60))
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        #задаем его местонахождение
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
    side = "left"
    #движение врага
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#класс элемента стены
class Wall(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height

        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface([self.width, self.height]) #создаем поверхность нужной ширины и длины
        self.image.fill(color) #заполняем ее цветом
 
       # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        draw.rect(window, self.color, (self.rect.x, self.rect.y, self.width, self.height))

init()
#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))

#создаем стены
w1 = Wall(color=(0, 0, 250), x=(win_width / 2 - win_width / 3), 
            y=(win_height / 2), width=300, height=10)
w2 = Wall(color=(0, 0, 250), x=410, y=(win_height / 2 - win_height / 4), width=10, height=350)

#создаем спрайты
packman = Player(player_image='Герои/pacman/pac-1.png', 
                    player_x=5, player_y=(win_height - 80), player_speed=5)
monster = Enemy('Герои/pacman/cyborg.png', win_width - 80, 200, 5)
final_sprite = GameSprite('Герои/pacman/pac-10.png', win_width - 85, win_height - 100, 0)

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
        monster.update()
        #обновляем их в новом местоположении при каждой итерации цикла
        packman.reset()
        monster.reset()
        final_sprite.reset()
    else:
        time.delay(4000)
        run = False
    #Проверка столкновения героя с врагом и стенами
    if (sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) 
            or sprite.collide_rect(packman, w2)):
        finish = True
        #вычисляем отношение
        img = image.load('gameover.jpeg')
        d = img.get_width() // img.get_height()
        window.fill((0, 0, 0))
        window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))
    if sprite.collide_rect(packman, final_sprite):
        finish = True
        img = image.load('Фоны/winner_1.jpg')
        window.fill((0, 0, 0))
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    
    display.update()

