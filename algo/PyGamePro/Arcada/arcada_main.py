# Подключить нужные модули
import pygame as pg

from arcada_sprites import *

# Основной цикл игры:
run = True 
finished = False

while run:
    # Обработка событий
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            run = False 
        elif event.type == pg.KEYDOWN: 
            if event.key == pg.K_LEFT:
                robin.x_speed = hero_speed * (-1)
            elif event.key == pg.K_RIGHT:
                robin.x_speed = hero_speed
            elif event.key == pg.K_UP:
                robin.jump(hero_jump * (-1))

        elif event.type == pg.KEYUP: 
            if event.key == pg.K_LEFT:
                robin.x_speed = 0
            elif event.key == pg.K_RIGHT:
                robin.x_speed = 0

    if not finished:
        # Перемещение игровых объектов 
        all_sprites.update()

        # дальше проверки правил игры
        # проверяем касание с бомбами:
        pg.sprite.groupcollide(bombs, all_sprites, True, True) 
                # если бомба коснулась спрайта, то она убирается из списка бомб, а спрайт - из all_sprites!

        # проверяем касание героя с врагами:
        if pg.sprite.spritecollide(robin, enemies, False):
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
        if pg.sprite.collide_rect(robin, pr):
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

    pg.display.update() 

    # Пауза
    pg.time.delay(20)