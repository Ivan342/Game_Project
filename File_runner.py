import pygame as pg
from pygame import time
from pygame.draw import *
from Personage import *
from level_constructor import *
from Falling_blocks import *

FPS = 60
clock = pg.time.Clock()
map_name = "Типокарта.txt"
time_scale = 1000
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
block = Block(screen)
pers = Personage(screen)
map = MAP()
'''
Здесь создаем карту как объект отдельного класса карт, чтобы к нему можно было обращаться из любой программы.
Класс прописан level_constructor
'''
map.read_map(map_name)
fall_raw = Fall_block_raw(screen)
spawn_filled = False
need_clean = False
game_speed = 0.5
start_time = time.get_ticks()
field = pg.image.load('фон1.jpg').convert()



while running:
    screen.blit(field,(0,0))
    for raw in raw_list:
        raw.fall()
        raw.draw()
        if raw.y > HEIGHT + raw.length:
            need_clean = True
        if raw_list[-1].y <= -raw.length + 100 + raw.length:
            spawn_filled = True

        else:
            spawn_filled = False


    if not spawn_filled:
        fall_raw.new_raw(screen, game_speed)
        spawn_filled = True
    if need_clean:
        raw_list = raw.clear()
        need_clean = False

    game_speed += raw_list[0].accel
    #map.map_chase(block, pers.x)
    map.draw_map(block, WIDTH / 2)
    pers.draw()
    pers.Collision_x(map.map_list)
    pers.Collision_y(map.map_list)
    pers.move_personage()
    #apers.Personage_animation_move_right(block, map)
    #pers.move_personage(block, map)
    dt = time.get_ticks() - start_time
    #print(dt)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pers.x = event.pos[0]
                pers.y = event.pos[1]
    pg.display.update()
    clock.tick(FPS)
    #print(clock.get_time())
pg.quit()
print(1)
