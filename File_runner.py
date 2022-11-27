import pygame as pg
from pygame.draw import *
from level_constructor import *

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
block = Block(screen)
map_list = read_map(map_name)

while running:
    screen.fill(TIME_COLOR)
    draw_map(block, map_list)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()
