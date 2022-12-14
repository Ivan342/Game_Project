import pygame as pg
from pygame import draw

menu_opened = True
level_chosen = False
surf_but = pg.Surface((230,60))
surf_but.set_alpha(200)
'''
тут создаются поверхности кнопок set_alpha-- прозрачность, pg.Surface--создание поверхности с размерами(...,...)
'''
WIDTH = 1200
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))


class Menu:
    def __init__(self):
        self.buttons = []
        self.menu_field =pg.image.load('фон меню.png').convert_alpha()

    def put_button(self, button):
        self.buttons.append(button)

    def draw_menu(self, screen):
        screen.blit(self.menu_field,(0,0))


        for butt in self.buttons:
            butt.draw(screen)


class Fal_blocks_lvl_but:
    def __init__(self,  x, y, len, wid, pic, text, name):
        self.x = x
        self.y = y
        self.length = len
        self.width = wid
        self.sprite = pic
        self.name = name
        self.pressed = False
        self.font = pg.font.Font(None, 45)
        self.text = self.font.render(text, True, (200, 200, 200))
        self.screen = screen

    def draw(self, screen):

        self.screen.blit(surf_but, (965,5))
        screen.blit(self.text, (self.x, self.y))

    def push_me(self):
        return "Типокарта.txt"


class Exit_button:
    def __init__(self, x, y, len, wid, pic, text, name):
        self.x = x
        self.y = y
        self.length = len
        self.width = wid
        self.sprite = pic
        self.name = name
        self.pressed = False
        self.font = pg.font.Font(None, 45)
        self.text = self.font.render(text, True, (200, 200, 200))
        self.screen = screen

    def draw(self, screen):
        self.screen.blit(surf_but, (965, 70))
        screen.blit(self.text, (self.x, self.y))

