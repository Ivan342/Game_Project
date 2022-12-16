import os

import pygame as pg

from GUNS import *
from Personage import *

GREY = (100, 100, 100)


class Bullet:
    def __init__(self, screen, gun, pers):
        """
        Инициализация пули
        """
        self.gun = gun
        self.pers = pers
        self.screen = screen
        self.Vx = 0
        self.Vy = 0
        self.direction = self.pers.direction
        if not self.direction:
            self.x = self.pers.x + self.gun.width
            self.y = self.pers.y + self.pers.height / 2
        else:
            self.x = self.pers.x - self.gun.width + 10
            self.y = self.pers.y + self.pers.height / 2
        self.color = GREY
        self.width_img = 12
        self.height_img = 12
        self.Vx_after_shot = 12
        self.Vy_after_shot = 0.1
        self.bullet_img = pg.image.load('графика/bullet.png').convert_alpha()

    def move_bullet(self):
        """
        Движение пули
        """
        g = 0.15
        self.Vy = self.Vy_after_shot
        if self.direction:
            self.Vy += g
            self.Vx = -self.Vx_after_shot
            self.x += self.Vx
            self.y += self.Vy
        else:
            self.Vy += g
            self.Vx = self.Vx_after_shot
            self.x += self.Vx
            self.y += self.Vy

    def draw_bullet(self):
        """
        Отрисовка пули
        """"
        self.screen.blit(self.bullet_img, (self.x, self.y))

    def direction_of_the_shot(self):
        """
        Определение направления, в котором вылетает пуля
        """
        if self.pers.Vx > 0:
            self.x = self.pers.x + self.pers.width / 3 + self.gun.width - 60
            self.y = self.pers.y + self.pers.height / 2 - 25
        elif self.pers.Vx <= 0:
            self.x = self.pers.x - self.gun.width / 2
            self.y = self.pers.y + self.pers.height / 2 - 25

    def collision(self, map):
        """
        Столкновение пули с картой
        """
        i = int(self.y) // 40
        j = int(self.x) // 40
        if map[i][j] != '0':
            return True
        i = int(self.y + self.height_img) // 40
        j = int(self.x + self.width_img) // 40
        if map[i][j] != '0':
            return True
        return False