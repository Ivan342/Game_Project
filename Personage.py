import pygame as pg


class Personage:
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.m = 10
        self.color = "red"
        self.Fy = 0
        self.radius = 40

    def interaction_with_keyboard(self, Vy, Vx):
        self.Vx = Vx
        self.Vy = Vy
        return 0

    def draw(self, screen, x, y):
        pg.draw.circle(screen, self.color, (x, y), self.radius)

    def move(self, x, y):
        x += self.Vx
        y += self.Vy
        return x, y
