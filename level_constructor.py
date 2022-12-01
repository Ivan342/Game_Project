import pygame as pg
from pygame.draw import *

WIDTH = 1200
HEIGHT = 600

GREY = (100, 100, 100)
LIGHT_GREY = (150, 150, 150)
DARK_GREY = (50, 50, 50)
BROWN = (40, 20, 10)
RED = (255, 0, 0)
GREEN = 0x00FF00
block_length = 40

TIME_COLOR = GREY


class Block:
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
        self.length = block_length
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
        self.screen.blit(self.grass, (x * self.length, y * self.length))

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


class MAP:
    """
    """

    def __init__(self):
        self.map_list = []

    def read_map(self, map_name):
        """
        1 - обычный блок
        2 - смертельный блок
        :param map_name: имя файла, в котором записана карта
        :return: массив строк, каждая из которых освечает за свою строку карты
        """
        with open(map_name) as file:
            for line in file.readlines():
                self.map_list.append(line.split())

    def draw_map(self, block, x):
        """
        Рисуем карту
        """
        for i in range(len(self.map_list)):
            for j in range(int((x - WIDTH/2)//block_length)-1, int((x + WIDTH/2)//block_length)+1):
                if self.map_list[i][j] == '1':
                    block.draw_block_grass(j - (x - WIDTH/2)//block_length , i)
                if self.map_list[i][j] == '2':
                    block.draw_block_under(j, i)
                if self.map_list[i][j] == '3':
                    block.draw_block_hill_left(j, i)

    def map_chase(self, block, pers_x):
        """
        Движение карты за игроком
        :param block:
        :param pers_x:
        :return:
        """
        if pers_x >= WIDTH / 2 and pers_x <= len(self.map_list[0]) * block.length - WIDTH / 2:
            self.draw_map(block, pers_x)
        elif pers_x < WIDTH / 2:
            self.draw_map(block, WIDTH/2)
        else:
            self.draw_map(block, len(self.map_list[0]) - WIDTH/2)
