import os

import pygame as pg

from GUNS import *
from Personage import *

GREY = (100, 100, 100)


class Bullet:
    def __init__(self, screen, gun, pers):
        self.gun = gun
        self.pers = pers
        self.screen = screen
        self.Vx = 0
        self.Vy = 0
        self.direction = self.pers.direction
        if not self.direction:
            self.x = self.pers.x + self.gun.width - 10
            self.y = self.pers.y
        else:
            self.x = self.pers.x - self.gun.width
            self.y = self.pers.y
        self.color = GREY
        self.width_img = 80
        self.height_img = 80
        self.Vx_after_shot = 12
        self.Vy_after_shot = 0.1
        self.bullet_img = pg.image.load('bullet.png').convert_alpha()

    def move_bullet(self):
        g = 0.15
        self.Vx = self.Vx_after_shot
        self.Vy = self.Vy_after_shot
        if self.direction:
            self.Vy += g
            self.x -= self.Vx
            self.y += self.Vy
        else:
            self.Vy += g
            self.x += self.Vx
            self.y += self.Vy





    def draw_bullet(self):
        #self.bullet_img.convert()
        self.bullet_img = pg.transform.scale(self.bullet_img, (self.width_img, self.height_img))
        self.screen.blit(self.bullet_img, (self.x, self.y))

    def direction_of_the_shot(self):
        if self.pers.Vx > 0:
            self.x = self.pers.x + self.pers.width / 3 + self.gun.width - 60
            self.y = self.pers.y + self.pers.height / 2 - 25
        elif self.pers.Vx <= 0:
            self.x = self.pers.x - self.gun.width / 2
            self.y = self.pers.y + self.pers.height / 2 - 25
