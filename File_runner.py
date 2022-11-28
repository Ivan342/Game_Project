import pygame as pg
from pygame.draw import *
from Personage import *
from level_constructor import *

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
block = Block(screen)
pers = Personage(screen)
map_list = read_map(map_name)
map = MAP(map_list)
'''
Здесь создаем карту как объект отдельного класса карт, чтобы к нему можно было обращаться из любой программы.
Класс прописан level_constructor
'''
while running:
    screen.fill(TIME_COLOR)
    draw_map(block, map_list)
    pers.move_x()
    pers.move_y()
    pers.interaction_with_keyboard()
    pers.draw()
    pers.Collision_x(map.map_list)
    pers.Collision_y(map.map_list)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pers.x = event.pos[0]
                pers.y = event.pos[1]

            pg.display.update()
    pg.display.update()
pg.quit()
