import pygame as pg
from pygame import draw
from random import randint

menu_opened = True
level_chosen = False
surf_but = pg.Surface((230,60))
surf_but.set_alpha(180)
surf_but_retry = pg.Surface((230,60))



'''
тут создаются поверхности кнопок set_alpha-- прозрачность, pg.Surface--создание поверхности с размерами(...,...)
'''
WIDTH = 1200
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))


class Menu:
    """
    Создание меню и его отрисовка.
    """
    def __init__(self):
        self.buttons = []
        self.menu_field =pg.image.load('графика/фон меню.png').convert_alpha()

    def put_button(self, button):
        self.buttons.append(button)

    def draw_menu(self, screen):
        screen.blit(self.menu_field,(0,0))


        for butt in self.buttons:
            butt.draw(screen)


class Fal_blocks_lvl_but:
    def __init__(self, x, y, len, wid, pic, text, name):
        """
        Создание кнопки, отправляющей игрока/-ов на уровень с падающими блоками и её отрисовка
        """
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

        self.screen.blit(surf_but, (self.x,self.y))
        screen.blit(self.text, (self.x, self.y+4))


    def push_me(self):
        names = ["Falling_Blocks_1", "Falling_Blocks_2"]
        return names[randint(0, 1)]


class Exit_button:
    """
    Создание кнопки выхода и её отрисовка
    """
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
        self.screen.blit(surf_but, (self.x, self.y))
        screen.blit(self.text, (self.x, self.y))

class Racing_lvl_but:
    """
    Создание кнопки, отправляющей игрока/-ов на гонку и её отрисовка
    """
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
        self.screen.blit(surf_but, (self.x, self.y))
        screen.blit(self.text, (self.x, self.y + 4))

    def push_me(self):
        return "Map_2"

class Color_battle_lvl_but:
    def __init__(self, x, y, len, wid, pic, text, name):
        """
        Создание кнопки, отправляющей игрока/-ов на уровень с падающими блоками и её отрисовка
        """
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

        self.screen.blit(surf_but, (self.x,self.y))
        screen.blit(self.text, (self.x, self.y+4))

    def push_me(self):
        names = ["Color_Battle_1", "Color_Battle_2"]
        return names[randint(0, 1)]

class Retry_but:
    def __init__(self, x, y, len, wid, pic, text, name):
        """
        Создание кнопки, отправляющей игрока/-ов на уровень с падающими блоками и её отрисовка
        """
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
        self.screen.blit(surf_but_retry, (self.x,self.y))
        screen.blit(self.text, (self.x, self.y+4))

class Back_to_menu_but:
    def __init__(self, x, y, len, wid, pic, text, name):
        """
        Создание кнопки, отправляющей игрока/-ов на уровень с падающими блоками и её отрисовка
        """
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

        self.screen.blit(surf_but, (self.x,self.y))
        screen.blit(self.text, (self.x, self.y+4))