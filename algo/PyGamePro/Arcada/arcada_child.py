# Подключить нужные модули
import pygame 

from arcada_sprites import *

pygame.init() 
# во время игры пишем надписи размера 72
font = pygame.font.Font(None, 72)

# Запуск игры
pygame.display.set_caption("ARCADA") 
window = pygame.display.set_mode([win_width, win_height])

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height)) 

# Основной цикл игры:
run = True 
finished = False

while run:
    # Обработка событий
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                robin.x_speed = -5 
            elif event.key == pygame.K_RIGHT:
                robin.x_speed = 5 
            elif event.key == pygame.K_UP:
                robin.jump(-7)

        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                robin.x_speed = 0
            elif event.key == pygame.K_RIGHT:
                robin.x_speed = 0

    if not finished:
        # Перемещение игровых объектов 
        all_sprites.update()

        # дальше проверки правил игры
        # проверяем касание с бомбами:
        pygame.sprite.groupcollide(bombs, all_sprites, True, True) 
                # если бомба коснулась спрайта, то она убирается из списка бомб, а спрайт - из all_sprites!

        # проверяем касание героя с врагами:
        if pygame.sprite.spritecollide(robin, enemies, False):
            robin.kill() # метод kill убирает спрайт из всех групп, в которых он числится

        # проверяем границы экрана: 
        if (
            robin.rect.x > right_bound and robin.x_speed > 0
            or
            robin.rect.x < left_bound and robin.x_speed < 0
        ): # при выходе влево или вправо переносим изменение в сдвиг экрана
            shift -= robin.x_speed  
            # перемещаем на общий сдвиг все спрайты (и отдельно бомбы, они ж в другом списке):
            for s in all_sprites:
                s.rect.x -= robin.x_speed # сам robin тоже в этом списке, поэтому его перемещение визуально отменится
            for s in bombs:
                s.rect.x -= robin.x_speed

        # Отрисовка
        # рисуем фон со сдвигом
        local_shift = shift % win_width 
        window.blit(back, (local_shift, 0)) 
        if local_shift != 0:
            window.blit(back, (local_shift - win_width, 0)) 

        # нарисуем все спрайты на экранной поверхности до проверки на выигрыш/проигрыш
        # если в этой итерации цикла игра закончилась, то новый фон отрисуется поверх персонажей
        all_sprites.draw(window)  
        # группу бомб рисуем отдельно - так бомба, которая ушла из своей группы, автоматически перестанет быть видимой
        bombs.draw(window)

        # проверка на выигрыш и на проигрыш:
        if pygame.sprite.collide_rect(robin, pr):
            finished = True
            window.fill(C_BLACK)
            # пишем текст на экране
            text = font.render("YOU WIN!", 1, C_RED)
            window.blit(text, (250, 250))

        # проверка на проигрыш:
        if robin not in all_sprites or robin.rect.top > win_height:
            finished = True            
            window.fill(C_BLACK) 
            # пишем текст на экране
            text = font.render("GAME OVER", 1, C_RED)
            window.blit(text, (250, 250))

    pygame.display.update() 

    # Пауза
    pygame.time.delay(20)