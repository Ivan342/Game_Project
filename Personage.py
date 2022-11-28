import pygame as pg
import keyboard  # using module keyboard


class Personage:
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.Vx = 0.1
        self.Vy = 0.1
        self.m = 10
        self.color = "red"
        self.Fy = 0
        self.radius = 40
        self.screen = screen
        self.acceleration = 0.0006
        self.width = 50
        self.height = 60

    def interaction_with_keyboard(self):
        if keyboard.is_pressed('w'):
            self.Vy -= self.acceleration
        elif keyboard.is_pressed('s'):
            self.Vy += self.acceleration
        elif keyboard.is_pressed('a'):
            self.Vx -= self.acceleration
        elif keyboard.is_pressed('d'):
            self.Vx += self.acceleration
        return 0

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move_x(self):
        self.x += self.Vx

    def move_y(self):
        self.y += self.Vy


