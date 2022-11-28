import pygame as pg
from pygame.draw import *

from Personage import *
from level_constructor import *

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
block = Block(screen)
p = Personage(screen)
map_list = read_map(map_name)

while running:
    screen.fill(TIME_COLOR)
    draw_map(block, map_list)
    p.draw(screen, 100, 50)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()
