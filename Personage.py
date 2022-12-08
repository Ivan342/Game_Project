import pygame
from pygame import time, draw

import pygame as pg
import keyboard

from level_constructor import *
w=0

class Personage:
    def __init__(self, screen):
        '''
        self.x координата левого вверхнего угла по горизонтали
        self.y - координата левого вверхнего угла по вертикали
        self.radius - костыль для упррощения, потому что сейчас персонаж это шарик.
        self.width - ширина персонажа, для нормальной отрисовки и проверки касаний собъектами. Считается от левого вверхнего угла
        self.height - высота персонажа для проверки касаний. Считается от левого вверхнего угла
        self.died - параметр смерти. 0-жив,1- мертв
        :param screen: экран, на который выводится персонаж
        '''
        self.screen = screen
        self.x = 100
        self.y = 300
        self.Vx = 0.1
        self.Vy = 0.1
        self.color = "red"
        self.screen = screen
        self.acceleration = 0.05
        self.width = 60
        self.height = 70
        self.onGround = False
        self.img = pg.image.load('girl0.png').convert_alpha()
        self.died = 0

    def move_personage(self, map):
        g = 0.1
        if keyboard.is_pressed('w'):
            if self.onGround:
                self.Vy = -5
                self.onGround = False
        elif keyboard.is_pressed('a'):
            self.Vx = -5
        elif keyboard.is_pressed('d'):
            self.Vx = 5
        elif (not keyboard.is_pressed('d')) & (not keyboard.is_pressed('d')):
            self.Vx = 0

        self.x += self.Vx

        #self.Collision_x(map)

        if not self.onGround:
            self.y += self.Vy
        self.Collision_y(map)

        print(self.onGround)
        if self.onGround == False:
            self.Vy += g
        return 0

    def move_personage_2(self, map):
        g = 0.1
        if keyboard.is_pressed('up arrow'):
            if self.onGround:
                self.Vy = -5
                self.onGround = False
        elif keyboard.is_pressed('left arrow'):
            self.Vx = -5
        elif keyboard.is_pressed('right arrow'):
            self.Vx = 5
        elif (not keyboard.is_pressed('left arrow')) & (not keyboard.is_pressed('right arrow')):
            self.Vx = 0

        self.x += self.Vx

        #self.Collision_x(map)

        if not self.onGround:
            self.y += self.Vy
        self.Collision_y(map)

        print(self.onGround)
        if self.onGround == False:
            self.Vy += g
        return 0
    def Personage_animation_move_right(self,block, mapik):
        '''
        анимация бега вправо и лево, стояния на месте
        '''
        global w
        animation_set = [pygame.image.load(f"girl{w}.png").convert_alpha() for w in range(0, 9)]
        animation_set_left = [pygame.image.load(f"girl_left{w}.png").convert_alpha() for w in range(0, 9)]
        if self.Vx>0:
            if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                self.screen.blit(animation_set[w], (WIDTH/2, int(self.y)))
            elif self.x < WIDTH / 2:
                self.screen.blit(animation_set[w], (int(self.x), int(self.y)))
            else:
                self.screen.blit(animation_set[w], (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        if self.Vx < 0:
            if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    self.screen.blit(animation_set_left[w], (WIDTH / 2, int(self.y)))
            elif self.x < WIDTH / 2:
                    self.screen.blit(animation_set_left[w], (int(self.x), int(self.y)))
            else:
                    self.screen.blit(animation_set_left[w],(- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))
        if self.Vx == 0:
            if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                self.screen.blit(self.img, (WIDTH / 2, int(self.y)))
            elif self.x < WIDTH / 2:
                self.screen.blit(self.img, (int(self.x), int(self.y)))
            else:
                self.screen.blit(self.img, (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))
        '''
        Почему у вас всегда скорость по игрикам больше нуля?
        '''
        w += 1
        if w == 8:
            w = 0





    def draw_fancy(self, block, mapik):
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
                        self.x = j * 40 - self.width
                        #self.Vx = min(self.Vx, 0)
                    if self.Vx < 0:
                        self.x = j * 40 + 40
                        #self.Vx = max(self.Vx, 0)

    def Collision_y(self, map):
        '''
        функция проверяет касание с блоками по y и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        for j in range(int(self.x) // 40, (int(self.x) + self.height) // 40 + 1):
            for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40 + 1):
                if map[i][j] == '1':
                    #print(i, j)
                    if self.Vy > 0:
                        self.y = i * 40 - self.height
                        #self.Vy = min(self.Vy, 0)
                        self.onGround = True
                    if self.Vy < 0:
                        self.y = i * 40 + 40
                        #self.Vy = max(self.Vy, 0)

