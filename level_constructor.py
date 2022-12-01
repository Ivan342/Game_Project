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
        self.length = 40
        self.screen = screen
        self.length = block_length

    def draw(self, x, y, color):
        rect(self.screen, color, ((x * self.length, y * self.length), (self.length, self.length)))





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

    def draw_map(self, block):
        """
        Рисуем карту
        """
        for i in range(len(self.map_list)):
            for j in range(len(self.map_list[i])):
                if self.map_list[i][j] == '1':
                    block.draw(j, i, LIGHT_GREY)
                if self.map_list[i][j] == '2':
                    block.draw(j, i, DARK_GREY)
                if self.map_list[i][j] == '3':
                    block.draw(j, i, BROWN)