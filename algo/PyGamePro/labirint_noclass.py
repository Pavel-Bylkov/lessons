from pygame import*
#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
 
image_hero = transform.scale(image.load('hero.png'), (80, 80))
speed_hero = 5
rect_hero = image_hero.get_rect()
rect.x_hero = 5
rect.y_hero = win_height - 80
 
side = "left"
image_enemy = transform.scale(image.load('cyborg.png'), (80, 80))
speed_enemy = 5
rect_enemy = image_enemy.get_rect()
rect.x_enemy = win_width - 80
rect.y_enemy = 200
 
wall_width = 300
wall_height = 10
wall_x = win_width / 2 - win_width / 3
wall_y = win_height / 2
 
image_final = transform.scale(image.load('treasure.png'), (80, 80))
rect_final = image_final.get_rect()
rect.x_final = win_width - 85
rect.y_final = win_height - 100
 
# картинка стены - прямоугольник нужных размеров и цвета:
image_wall = Surface([wall_width, wall_height])
image_wall.fill((0, 0, 0))
rect_wall = image_wall.get_rect()
rect_wall = Rect(wall_x, wall_y, wall_width, wall_height)
 
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
 
#проверка, что игра еще не завершена
  if not finish:
       #обновляем фон каждую итерацию
       window.fill((255, 255, 255))
  
       #рисуем стены
       draw.rect(window, (0, 0, 0), (wall_x, wall_y, wall_width, wall_height))
       #запускаем движения спрайтов
       keys = key.get_pressed()
       if keys[K_LEFT] and rect.x_hero > 5:
           rect.x_hero -= speed_hero
       if keys[K_RIGHT] and rect.x_hero < win_width - 80:
           rect.x_hero += speed_hero
       if keys[K_UP] and rect.y_hero > 5:
           rect.y_hero -= speed_hero
       if keys[K_DOWN] and rect.y_hero < win_height - 80:
           rect.y_hero += speed_hero
      
      
       if rect.x_enemy <= 410:
           side = "right"
       if rect.x_enemy >= win_width - 85:
           side = "left"
       if side == "left":
           rect.x_enemy -= speed_enemy
       else:
           rect.x_enemy += speed_enemy
      
       #обновляем их в новом местоположении при каждой итерации цикла
       window.blit(image_hero, (rect.x_hero, rect.y_hero))
       window.blit(image_enemy, (rect.x_enemy, rect.y_enemy))
       window.blit(image_final, (rect.x_final, rect.y_final))
 
  display.update()
