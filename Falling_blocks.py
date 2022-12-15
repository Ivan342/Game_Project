import pygame as pg
from pygame.draw import *
from level_constructor import *
from random import randint
from Personage import*

raw_list = []
list_pos_x = []

class Fall_block_raw():

    def __init__(self, screen):
        self.length = 40
        self.accel = 0.0005
        self.raw_list = []
        self.screen = screen
        self.block_pos = [randint(0, 10) for i in range(int(WIDTH / self.length))]
        self.y = -self.length
        self.vy = 0
        self.bomb = pg.image.load('kimm.png').convert_alpha()

    def new_raw(self, screen, vely):
        """
        Обьявление новой строки падающих блоков
        :param screen: то, куда рисовать
        :param vely: начальная скорость падения
        :return:
        """

        new_raw = Fall_block_raw(screen)
        new_raw.vy = vely
        self.raw_list.append(new_raw)







    def fall(self):
        """
        Падение блоков
        :return:
        """
        self.y += self.vy
        self.vy += self.accel

    def draw(self):
        """
        Отрисовка блоков
        :return:
        """
        #print(self.block_pos)
        for i in range(len(self.block_pos)):
            if self.block_pos[i] == 0:
                self.screen.blit(self.bomb, ((i * self.length, self.y-20), (self.length, self.length)))

    def clear(self):
        """
        Удаление строки
        :return:
        """
        self.raw_list = self.raw_list[1:]
