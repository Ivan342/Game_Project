import pygame as pg
from pygame.draw import *

map_name = "Типокарта.txt"
WIDTH = 1200
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
GREY = (100, 100, 100)
LIGHT_GREY = (150, 150, 150)
DARK_GREY = (50, 50, 50)
BROWN = (40, 20, 10)

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
    def __init__(self):
        self.length = 40
        self.screen = screen

    def draw(self, x, y, color):
        rect(self.screen, color, ((x * self.length, y * self.length), (self.length, self.length)))





def draw_map():
    """
    Рисуем карту
    """
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == '1':
                block.draw(j, i, LIGHT_GREY)
            if map_list[i][j] == '2':
                block.draw(j, i, DARK_GREY)
            if map_list[i][j] == '3':
                block.draw(j, i, BROWN)

block = Block()
map_list = read_map(map_name)