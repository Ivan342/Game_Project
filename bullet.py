import pygame as pg

GREY = (100, 100, 100)


class Bullet:
    def __init__(self, screen):
        self.screen = screen
        self.Vx = 0
        self.Vy = 0
        self.x = 0
        self.y = 0
        self.radius = 5
        self.color = GREY
        self.img_bullet = pg.image.load('bullet.png').convert_alpha()

    def move_bullet(self, Vx_after_shot, Vy_after_shot):
        g = 0.15
        self.Vx = Vx_after_shot
        self.Vy = Vy_after_shot
        self.Vy += g

    def draw_bullet(self):
        imagerect = self.img_bullet.get_rect()
        self.screen.blit(self.img_bullet, imagerect)
