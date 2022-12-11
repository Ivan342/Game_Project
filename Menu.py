import pygame as pg
from pygame import draw

menu_opened = True
level_chosen = False


class Menu:
    def __init__(self):
        self.buttons = []

    def put_button(self, button):
        self.buttons.append(button)

    def draw_menu(self, screen):
        screen.fill((150, 150, 0))
        """ 
        FIXME: надо добавить тесктуры заднему фону меню
        """
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
        self.font = pg.font.Font(None, 50)
        self.text = self.font.render(text, True, (255, 255, 255))

    def draw(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.length, self.width))
        screen.blit(self.text, (self.x, self.y))
        """ 
        FIXME: надо добавить тесктуры кнопке
        """
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
        self.font = pg.font.Font(None, 50)
        self.text = self.font.render(text, True, (255, 255, 255))

    def draw(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.length, self.width))
        screen.blit(self.text, (self.x, self.y))
        """ 
        FIXME: надо добавить тесктуры кнопке
        """