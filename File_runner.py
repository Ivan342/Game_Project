import pygame as pg
from pygame import time
from pygame.draw import *
from Personage import *
from level_constructor import *
from Falling_blocks import *

time_scale = 1000
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
block = Block(screen)
pers = Personage(screen)
map_list = read_map(map_name)
map = MAP(map_list)
fall_raw = Fall_block_raw(screen)
spawn_filled = False
need_clean = False
game_speed = 0.5
start_time = time.get_ticks()

'''
Здесь создаем карту как объект отдельного класса карт, чтобы к нему можно было обращаться из любой программы.
Класс прописан level_constructor
'''
while running:
    screen.fill(TIME_COLOR)
    for raw in raw_list:
        raw.fall()
        # raw.draw()
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
    draw_map(block, map_list)

    pers.draw()
    # pers.Collision_x(map.map_list)
    # pers.Collision_y(map.map_list)
    pers.move_personage()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pers.x = event.pos[0]
                pers.y = event.pos[1]
    pg.display.update()
pg.quit()
