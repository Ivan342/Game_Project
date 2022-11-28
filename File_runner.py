import pygame as pg
from pygame.draw import *
from pynput.mouse import Controller
from Personage import *
from level_constructor import *

pg.init()
mouse = Controller()
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
block = Block(screen)
p = Personage(screen)
map_list = read_map(map_name)

while running:
    screen.fill(TIME_COLOR)
    draw_map(block, map_list)
    p.draw(screen, mouse.click[0], mouse.position[1])
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()
