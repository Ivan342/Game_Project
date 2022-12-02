import pygame
from pygame import time, draw

import pygame as pg
import keyboard

from level_constructor import *
trace = ([])
w=0


def draw_point(m, color, screen):
    for [i, j] in m:
        draw.circle(screen, color, (i, j), 1)





class Personage:
    def __init__(self, screen):
        '''
        self.x координата левого вверхнего угла по горизонтали
        self.y - координата левого вверхнего угла по вертикали
        self.radius - костыль для упррощения, потому что сейчас персонаж это шарик.
        self.width - ширина персонажа, для нормальной отрисовки и проверки касаний собъектами. Считается от левого вверхнего угла
        self.height - высота персонажа для проверки касаний. Считается от левого вверхнего угла
        :param screen: экран, на который выводится персонаж
        '''
        self.screen = screen
        self.x = 100
        self.y = 300
        self.Vx = 0.1
        self.Vy = 0.1
        self.color = "red"
        self.Fy = 0
        self.radius = 40
        self.screen = screen
        self.acceleration = 0.05
        self.width = 50
        self.height = 60
        self.trace = trace

    def move_personage(self):
        g = 0.006
        if keyboard.is_pressed('w'):
            self.Vy -= self.acceleration
        elif keyboard.is_pressed('s'):
            self.Vy += self.acceleration
        elif keyboard.is_pressed('a'):
            self.Vx -= self.acceleration
        elif keyboard.is_pressed('d'):
            self.Vx += self.acceleration

        self.trace.append([self.x, self.y])
        draw_point(trace, self.color, self.screen)

        self.x += self.Vx

        if not self.on_ground(map):
            self.Vy += g

        self.y += self.Vy
        return 0

    def Personage_animation_move_right(self,block, mapik):
        global w
        animation_set = [pygame.image.load(f"stick{w}.png") for w in range(1, 4)]
        if self.Vx>0:
            if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                self.screen.blit(animation_set[w], (WIDTH/2, int(self.y)))
            elif self.x < WIDTH / 2:
                self.screen.blit(animation_set[w], (int(self.x), int(self.y)))
            else:
                self.screen.blit(animation_set[w], (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))


            w += 1
            if w == 3:
                w = 0

    def draw(self):
        pg.draw.rect(self.screen, self.color, (int(self.x), int(self.y), self.width, self.height))

    def draw(self, block, mapik):
        if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
            pg.draw.rect(self.screen, self.color, (WIDTH/2, self.y, self.width, self.height))
        elif self.x < WIDTH / 2:
            pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            pg.draw.rect(self.screen, self.color, (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, self.y, self.width, self.height))


    def Collision_x(self, map):
        '''
        функция проверяет касание с блоками по x и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        for j in range(int(self.x) // 40, (int(self.x) + self.height) // 40 + 1):
            for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40 + 1):
                if map[i][j] == '1':
                    if self.Vx > 0:
                        self.x = int(self.x) - ((int(self.x) + self.width) % 40)
                        self.Vx = min(self.Vx, 0)
                    if self.Vx < 0:
                        self.x = int(self.x) + 40 - (int(self.x) % 40)
                        self.Vx = max(self.Vx, 0)

    def Collision_y(self, map):
        '''
        функция проверяет касание с блоками по y и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        for j in range(int(self.x) // 40, (int(self.x) + self.height) // 40 + 1):
            for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40 + 1):
                if map[i][j] == '1':
                    if self.Vy > 0:
                        self.y = int(self.y) - ((int(self.y) + self.height) % 40)
                        self.Vy = min(self.Vy, 0)
                    if self.Vy < 0:
                        self.y = int(self.y) + 40 - (int(self.y) % 40)
                        self.Vy = max(self.Vy, 0)

    def on_ground(self, map):
        i = min((int(self.y) + self.height) // 40 + 1, 14)
        for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40 + 1):
            if (map.map_list[i][j] == '1' or map.map_list[i][j] == '2' or map.map_list[i][j] == '3') and (self.y % 40) < 2:
                return True
            else:
                return False
print(1)