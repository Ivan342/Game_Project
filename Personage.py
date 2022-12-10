import pygame
from Falling_blocks import*
from pygame import time, draw

import pygame as pg
import keyboard

from level_constructor import *

w = 0
FPS = 60
clock = pg.time.Clock()


class Personage:
    def __init__(self, screen):
        '''
        self.x координата левого вверхнего угла по горизонтали
        self.y - координата левого вверхнего угла по вертикали
        self.radius - костыль для упррощения, потому что сейчас персонаж это шарик.
        self.width - ширина персонажа, для нормальной отрисовки и проверки касаний собъектами.
        Считается от левого вверхнего угла
        self.height - высота персонажа для проверки касаний. Считается от левого вверхнего угла
        :param screen: экран, на который выводится персонаж
        self.died - показатель смерти. 0-жив, 1-мертв(от взрыва)(если будете добавлять другие источники смерти,
        то обозначайте их другими цифрами, чтобы разделять анимаwии)
        '''
        self.screen = screen
        self.x = 100
        self.y = 300
        self.Vx = 0.1
        self.Vy = 0.1
        self.color = "red"
        self.screen = screen
        self.acceleration = 0.3
        self.width = 60
        self.height = 70
        self.onGround = False
        self.direction = False
        self.img = pg.image.load('girl0.png').convert_alpha()
        self.img_left = pg.image.load('girl_left2.png').convert_alpha()
        self.block_jump_speed = 5
        self.died = 0

        self.power_up = 15
        self.time_after_up = 0

    def start_game(self):
        self.died=0


    def move_personage(self, map):
        g = 0.15
        '''
        if keyboard.is_pressed('w'):
            if self.onGround and self.power_up <= 37:
                self.power_up += 1
        if ( not keyboard.is_pressed('w') ) and self.power_up != 10 and self.onGround:
            self.Vy = -1*12*(self.power_up / 60)
            self.power_up = 0
            self.onGround = False
        '''
        if self.Vy < 0 or self.onGround:
            if keyboard.is_pressed('w') and self.time_after_up < 20:

                self.Vy = -4
                self.onGround = False
                self.time_after_up += 1

        if self.Vy >= 0:
            self.time_after_up = 0

        if keyboard.is_pressed('a') and self.Vx <= 5 and self.Vx >= -5:
            self.Vx -= self.acceleration
            self.direction = True
        if keyboard.is_pressed('d') and self.Vx <= 5 and self.Vx >= -5:
            self.Vx += self.acceleration
            self.direction = False

        #if keyboard.is_pressed('s'):
        #    self.Vy += self.acceleration
        #elif keyboard.is_pressed('d'):
        #    self.Vx = 5
        #elif (not keyboard.is_pressed('a')) & (not keyboard.is_pressed('d')):
        if self.Vx > 0 and (not keyboard.is_pressed('d')):
            self.Vx -= 2 * self.acceleration
            if self.Vx >= -0.5 and self.Vx <= 0.5:
                self.Vx = 0

        if self.Vx < 0 and (not keyboard.is_pressed('a')):
            self.Vx += 2 * self.acceleration
            if self.Vx >= -0.5 and self.Vx <= 0.5:
                self.Vx = 0


        self.x += self.Vx
        self.Collision_x(map)

        self.Collision_y(map)
        if not self.onGround:
            self.y += self.Vy

        self.Collision_y(map)

        #print(self.onGround)
        if self.onGround == False:
            self.Vy += g

        return 0


    def death_animations(self):
        '''
        Анимации смертей
        '''
        global w
        animation_set_explosion = [pygame.image.load(f"explosion{w}.png").convert_alpha() for w in range(0, 10)]
        for i in range(6):
            self.screen.blit(animation_set_explosion[i], (int(self.x), int(self.y)))
            clock.tick(8)
            pg.display.update()






    def collusion_with_red_block(self):
        '''
        Функция проверяет пересечение Кима и персонажа
        '''
        for raw in raw_list:

            #print(raw.y, self.y, list_pos_x)
            if (self.y >(raw.y-20) and self.y<(raw.y+40)) or (self.y+45 >(raw.y) and (self.y+45)<(raw.y+40))   :
                #print('gbjkdfbsdkjf gshjkbhjsbgmnbjgkbdrdkjgerjkngkjrengjkrngjklenfljnweilgnljwebglirgjrbgjberkjberkgberbgj')
                for i in range(len(raw.block_pos)):
                    if raw.block_pos[i]==0:
                        if (((self.x+30)>i*40) and (self.x+30)<(i*40+40)):
                            #print(uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuy')
                            if self.died == 0:
                                self.died=1






    def move_personage_2(self, map):
        g = 0.1
        if keyboard.is_pressed('up arrow'):
            if self.onGround and self.power_up <= 37:
                self.power_up += 1

        if ( not keyboard.is_pressed('up arrow') ) and self.power_up != 2 and self.onGround:
            self.Vy = -1*10*(self.power_up / 60)
            self.power_up = 0
            self.onGround = False
        elif keyboard.is_pressed('left arrow'):
            self.Vx = -5
            self.direction = True
        elif keyboard.is_pressed('right arrow'):
            self.Vx = 5
            self.direction = False
        elif (not keyboard.is_pressed('left arrow')) & (not keyboard.is_pressed('right arrow')):
            self.Vx = 0

        self.x += self.Vx

        self.Collision_x(map)

        if not self.onGround:
            self.y += self.Vy
        self.Collision_y(map)

        #print(self.onGround)
        if self.onGround == False:
            self.Vy += g
        return 0

    def Personage_animation_move_right(self, block, mapik):
        '''
        анимация бега вправо и лево, стояния на месте
        '''
        global w
        animation_set = [pygame.image.load(f"girl{w}.png").convert_alpha() for w in range(0, 9)]
        animation_set_left = [pygame.image.load(f"girl_left{w}.png").convert_alpha() for w in range(0, 9)]
        if self.Vx > 0:
            if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                self.screen.blit(animation_set[w], (WIDTH / 2, int(self.y)))
            elif self.x < WIDTH / 2:
                self.screen.blit(animation_set[w], (int(self.x), int(self.y)))
            else:
                self.screen.blit(animation_set[w],
                                 (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        if self.Vx < 0:
            if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                self.screen.blit(animation_set_left[w], (WIDTH / 2, int(self.y)))
            elif self.x < WIDTH / 2:
                self.screen.blit(animation_set_left[w], (int(self.x), int(self.y)))
            else:
                self.screen.blit(animation_set_left[w],
                                 (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))
        if self.Vx == 0:
            if self.direction:
                if self.x >= WIDTH / 2 and self.x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    self.screen.blit(self.img_left, (WIDTH / 2, int(self.y)))
                elif self.x < WIDTH / 2:
                    self.screen.blit(self.img_left, (int(self.x), int(self.y)))
                else:
                    self.screen.blit(self.img_left,
                                     (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))
            else:
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
            pg.draw.rect(self.screen, self.color, (WIDTH / 2, self.y, self.width, self.height))
        elif self.x < WIDTH / 2:
            pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            pg.draw.rect(self.screen, self.color,
                         (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, self.y, self.width, self.height))

    def Collision_x(self, map):
        '''
        функция проверяет касание с блоками по x и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        if self.Vx >= 0:
            for j in range(int(self.x) // 40 + 1, (int(self.x) + self.height) // 40 + 1):
                for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40):
                    if map[i][j] != '0':
                        self.x = j * 40 - self.width
                        self.Vx = 0

        if self.Vx < 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.height) // 40):
                for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40):
                    if map[i][j] != '0':
                        self.x = (j + 1) * 40
                        self.Vx = 0

    def Collision_y(self, map):
        '''
        функция проверяет касание с блоками по y и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        if self.Vy >= 0:
            for j in range(int(self.x) // 40 , (int(self.x) + self.width) // 40 ):
                for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40 + 1):
                    if map[i][j] != '0':
                        self.y = i * 40 - self.height
                        self.Vy = 0
                        self.onGround = True
                        #print(0)
                        if map[i][j] == '4':
                            #print(1)
                            self.Vy -= self.block_jump_speed
                    else:
                        self.onGround = False

        if self.Vy < 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40 + 1):
                for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40):
                    if map[i][j] != '0':
                        self.y = (i+1) * 40
                        self.Vy = 0
                        # self.Vy = max(self.Vy, 0)
