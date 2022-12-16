import pygame as pg
from pygame import draw
from random import randint

WIDTH = 1200
HEIGHT = 900

GREY = (100, 100, 100)
LIGHT_GREY = (150, 150, 150)
DARK_GREY = (50, 50, 50)
BROWN = (40, 20, 10)
RED = (255, 0, 0)
GREEN = 0x00FF00
block_length = 40
PURPLE = (154, 50, 205)
YELLOW = (200, 200, 0)
BLUE = (0, 0, 200)
VIOLET = (120, 100, 255)

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
        self.screen = screen
        self.length = block_length
        self.screen = screen
        self.stone = pg.image.load('графика/grass.png').convert_alpha()
        self.grass_box = self.stone.get_rect()
        self.ground = pg.image.load('графика/brick_flat.png').convert_alpha()
        self.ground_box = self.stone.get_rect()
        self.finish_flag = pg.image.load('графика/флаг.png').convert_alpha()
        self.hill_box = self.stone.get_rect()
        self.vine0 = pg.image.load('графика/vine0.png').convert_alpha()
        self.vine1 = pg.image.load('графика/vine1.png').convert_alpha()
        self.vine2 = pg.image.load('графика/vine2.png').convert_alpha()
        self.jump_block = pg.image.load('графика/jump_block.png').convert_alpha()
        self.death_block = pg.image.load('графика/death.png').convert_alpha()
        self.brick = pg.image.load('графика/brick.png').convert_alpha()

    def draw_block_stone(self, x, y):
        '''
        рисует каменный блок
        '''
        self.screen.blit(self.stone, (x * self.length, y * self.length))

    def draw_brick(self, x, y):
        '''
        рисует каменный блок
        '''
        self.screen.blit(self.brick, (x * self.length, y * self.length))

    def draw_block_under(self, x, y):
        '''
        рисует блок без травы (земля под травой)
        '''
        self.screen.blit(self.ground, (x * self.length, y * self.length))

    def draw_finish_block(self, x, y):
        '''
        рисует блок финиша
        '''
        self.screen.blit(self.finish_flag, (x * self.length, y * self.length))

    def draw_block_jump(self, x, y):
        '''
        рисует прыгучий блок
        '''
        self.screen.blit(self.jump_block, (x * self.length, y * self.length))

    def draw_pers1(self, x, y):
        '''
        рисует блок перекрашенный первым персонажем
        '''
        draw.rect(self.screen, VIOLET, (x * self.length, y * self.length, block_length, block_length))

    def draw_pers2(self, x, y):
        '''
        рисует блок перекрашенный вторым персонажем
        '''
        draw.rect(self.screen, PURPLE, (x * self.length, y * self.length, block_length, block_length))

    def draw_deadly_block(self, x, y):
        '''
        рисует смертульный блок
        '''
        self.screen.blit(self.death_block, (x * self.length, y * self.length))

    def draw_vine0_block(self, x, y):
        '''
        рисует лиану 0
        '''
        self.screen.blit(self.vine0, (x * self.length, y * self.length))

    def draw_vine1_block(self, x, y):
        '''
        рисует лиану 1
        '''
        self.screen.blit(self.vine1, (x * self.length, y * self.length))

    def draw_vine2_block(self, x, y):
        '''
        рисует лиану 2
        '''
        self.screen.blit(self.vine2, (x * self.length, y * self.length))


class MAP:
    """
    Создание класса карты
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

        :param block: вызываем функции класса block
        :param x: Позиция игрока по оси x

        Типы блоков:
        0 - пустота (без блока)
        1 - блок с травой
        2 - гладкий камень
        3 - финиш
        4 - пружинный блок
        5 - смертельный блок
        6 - цвет 1 игрока
        7 - цвет 2 игрока
        8 - лиана 1
        9 - лиана 2
        10 - лиана 3
        11 - кирпич не гладкий
        """
        if int((x + WIDTH / 2) // block_length) + 1 > len(self.map_list[0]):
            draw_distance = int((x + WIDTH / 2) // block_length) - 1
        else:
            draw_distance = int((x + WIDTH / 2) // block_length)
        for i in range(len(self.map_list)):
            for j in range(int((x - WIDTH / 2) // block_length), draw_distance + 1):
                if self.map_list[i][j] == '1':
                    block.draw_block_stone(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '2':
                    block.draw_block_under(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '3':
                    block.draw_finish_block(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '4':
                    block.draw_block_jump(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '6':
                    block.draw_pers1(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '7':
                    block.draw_pers2(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '5':
                    block.draw_deadly_block(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '8':
                    block.draw_vine0_block(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '9':
                    block.draw_vine1_block(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '10':
                    block.draw_vine2_block(j - (x - WIDTH / 2) / block_length, i)
                if self.map_list[i][j] == '11':
                    block.draw_brick(j - (x - WIDTH / 2) / block_length, i)

    def map_chase(self, block, pers_x):
        """
        Движение карты за игроком
        :param block:
        :param pers_x:
        :return:
        """
        if WIDTH / 2 <= pers_x <= len(self.map_list[0]) * block.length - WIDTH / 2:
            self.draw_map(block, pers_x)
        elif pers_x < WIDTH / 2:
            self.draw_map(block, WIDTH / 2)
        else:
            self.draw_map(block, len(self.map_list[0]) * block.length - WIDTH / 2)
