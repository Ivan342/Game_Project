
import pygame as pg
from pygame.draw import *


map_name = "Типокарта.txt"
WIDTH = 1200
HEIGHT = 600


GREY = (100, 100, 100)
LIGHT_GREY = (150, 150, 150)
DARK_GREY = (50, 50, 50)
BROWN = (40, 20, 10)
WHITE = (255,255,255)

TIME_COLOR = GREY


def read_map(map_name):
    """
    :param map_name: имя файла, в котором записана карта
    :return: массив строк, каждая из которых освечает за свою строку карты
    """
    ll = []
    with open(map_name) as file:
        for line in file.readlines():
            ll.append(line.split())

    return ll


class Block():
    def __init__(self, screen):

        '''
        :param screen:
        :param pic: берет картинку для блоков и вставляет ее на указанных координатах
        self.grass открывает картинку травы
        self.ground Открывает картинку земли
        self.hill открывает картинку склона
        '''
        self.length = 40
        self.screen = screen
        self.grass = pg.image.load('землятрава.jpg').convert()
        self.grass_box = self.grass.get_rect()
        self.ground = pg.image.load('земля.jpg').convert()
        self.ground_box = self.grass.get_rect()
        self.hill_left = pg.image.load('склон_лево.png').convert_alpha()
        self.hill_box = self.grass.get_rect()
    def draw_block_grass(self, x, y):
        '''
        рисует блок с травой
        '''
        self.screen.blit(self.grass, (x*self.length,y*self.length))
    def draw_block_under(self, x, y):
        '''
        рисует блок без травы (земля под травой)
        '''
        self.screen.blit(self.ground, (x * self.length, y * self.length))

    def draw_block_hill_left(self, x, y):
        '''
        рисует блок склона(левого)
        '''
        self.screen.blit(self.hill_left, (x * self.length, y * self.length))



def draw_map(block, map_list):
    """
    Рисуем карту
    """

    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == '1':
                block.draw_block_grass(j, i)
            if map_list[i][j] == '2':
                block.draw_block_under(j, i)
            if map_list[i][j] == '3':
                block.draw_block_hill_left(j, i)



