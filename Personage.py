import pygame
from Falling_blocks import*
from pygame import time, draw

import pygame as pg
import keyboard

from level_constructor import *
my_time=0
surf_wasted = pygame.Surface((1200,600))
surf_wasted.set_alpha(20)

w = 0
FPS = 60
clock = pg.time.Clock()
prozrachost=0

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
        self.block_jump_speed = 10
        self.died = 0
        self.surf_wasted_img = pygame.image.load('wasted.png').convert_alpha()

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

        if self.Vx > 0 and (not keyboard.is_pressed('d')):
            self.Vx -= 2 * self.acceleration
            if self.Vx >= -0.5 and self.Vx <= 0.5:
                self.Vx = 0

        if self.Vx < 0 and (not keyboard.is_pressed('a')):
            self.Vx += 2 * self.acceleration
            if self.Vx >= -0.5 and self.Vx <= 0.5:
                self.Vx = 0

        self.y += self.Vy
        if not self.onGround:
            self.Vy += g
        self.onGround = False
        self.Collision_y(map)

        self.x += self.Vx
        self.Collision_x(map)

        #pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height)) # отладка

        return 0


    def death_animations(self):
        '''
        Анимации смертей
        '''

        global w,my_time,prozrachost
        death_screen = True
        animation_set_explosion = [pygame.image.load(f"explosion{w}.png").convert_alpha() for w in range(0, 10)]
        for i in range(6):
            self.screen.blit(animation_set_explosion[i], (int(self.x), int(self.y)))
            clock.tick(8)
            pg.display.update()
        while death_screen:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    death_screen = False

            my_time+=1
            clock.tick(30)
            self.screen.blit(surf_wasted, (0,0))
            pg.display.update()

            if my_time>=25:
                self.surf_wasted_img.set_alpha(prozrachost)
                self.screen.blit(self.surf_wasted_img, (456,230))
                pg.display.update()
                clock.tick(30)
                prozrachost+=8

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
                            #print(Huuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuy')
                            if self.died == 0:
                                self.died=1

    def move_personage_2(self, map):
        g = 0.15
        if self.Vy < 0 or self.onGround:
            if keyboard.is_pressed('up_arrow') and self.time_after_up < 20:
                self.Vy = -4
                self.onGround = False
                self.time_after_up += 1

        if self.Vy >= 0:
            self.time_after_up = 0

        if keyboard.is_pressed('left_arrow') and self.Vx <= 5 and self.Vx >= -5:
            self.Vx -= self.acceleration
            self.direction = True
        if keyboard.is_pressed('right_arrow') and self.Vx <= 5 and self.Vx >= -5:
            self.Vx += self.acceleration
            self.direction = False

        if self.Vx > 0 and (not keyboard.is_pressed('right_arrow')):
            self.Vx -= 2 * self.acceleration
            if self.Vx >= -0.5 and self.Vx <= 0.5:
                self.Vx = 0

        if self.Vx < 0 and (not keyboard.is_pressed('left_arrow')):
            self.Vx += 2 * self.acceleration
            if self.Vx >= -0.5 and self.Vx <= 0.5:
                self.Vx = 0

        self.y += self.Vy
        if not self.onGround:
            self.Vy += g
        self.onGround = False
        self.Collision_y(map)

        self.x += self.Vx
        self.Collision_x(map)

        # pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height)) # отладка

        return 0

    def Personage_animation_moveemnt(self, block, mapik, max_pers_x):
        '''
        анимация бега вправо и лево, стояния на месте
        '''
        global w
        animation_set = [pygame.image.load(f"girl{w}.png").convert_alpha() for w in range(0, 9)]
        animation_set_left = [pygame.image.load(f"girl_left{w}.png").convert_alpha() for w in range(0, 9)]
        if self.Vx > 0:
            if max_pers_x >= WIDTH / 2 and max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:
                    print()
                    self.screen.blit(animation_set[w], (WIDTH / 2, int(self.y)))
                else:
                    print(23)
                    self.screen.blit(animation_set[w], (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(animation_set[w], (int(self.x), int(self.y)))

            else:

                self.screen.blit(animation_set[w],
                                 (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))


        if self.Vx < 0:
            if max_pers_x >= WIDTH / 2 and max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:
                    print(18)
                    self.screen.blit(animation_set_left[w], (WIDTH / 2, int(self.y)))
                else:
                    print(17)
                    self.screen.blit(animation_set_left[w], (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(animation_set_left[w], (int(self.x), int(self.y)))
            else:

                self.screen.blit(animation_set_left[w],
                                     (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        if self.Vx == 0:
            if self.direction:
                if max_pers_x >= WIDTH / 2 and max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    if self.x == max_pers_x:
                        print(1)
                        self.screen.blit(self.img_left, (WIDTH / 2, int(self.y)))
                    else:
                        print(2)
                        self.screen.blit(self.img_left, (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
                elif max_pers_x < WIDTH / 2:

                    self.screen.blit(self.img_left, (int(self.x), int(self.y)))
                else:

                    self.screen.blit(self.img_left,
                                     (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

            else:
                if max_pers_x >= WIDTH / 2 and max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    if self.x == max_pers_x:
                        print(7)
                        self.screen.blit(self.img, (WIDTH / 2, int(self.y)))
                    else:
                        print(8)
                        self.screen.blit(self.img, (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
                elif max_pers_x < WIDTH / 2:

                    self.screen.blit(self.img, (int(self.x), int(self.y)))
                else:
                    self.screen.blit(self.img,
                                         (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        '''
        Почему у вас всегда скорость по игрикам больше нуля?
        '''
        w += 1
        if w == 8:
            w = 0



    def Collision_x(self, map):
        '''
        функция проверяет касание с блоками по x и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        if self.Vx > 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40 + 1):
                for i in range(int(self.y + 1) // 40, (int(self.y - 1) + self.height) // 40 + 1):
                    #pg.draw.rect(self.screen, "black", (j * 40, i * 40, 10, 10))  # отладка
                    if map[i][j] != '0':
                        self.x = j * 40 - self.width
                        #pg.draw.rect(self.screen, "black", (j * 40, i * 40, 10, 10)) # отладка
                        #print(i, j)

        if self.Vx < 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40):
                for i in range(int(self.y + 1) // 40, (int(self.y - 1) + self.height) // 40 + 1):
                    #pg.draw.rect(self.screen, "black", (j * 40, i * 40, 10, 10))  # отладка
                    if map[i][j] != '0':
                        self.x = (j + 1) * 40
                        #pg.draw.rect(self.screen, "black", (j * 40, i * 40, 10, 10)) # отладка
                        #print(i, j)

    def Collision_y(self, map):
        '''
        функция проверяет касание с блоками по y и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        if self.Vy > 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40):
                for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40 + 1):
                    if map[i][j] != '0':
                        self.y = i * 40 - self.height
                        self.Vy = 0
                        self.onGround = True
                        # print(0)
                    else:
                        if map[i][j] == '4':
                            #print(1)
                            #print(self.Vy)
                            self.Vy -= self.block_jump_speed
                        self.onGround = False

        if self.Vy < 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40):
                for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40+1):
                    if map[i][j] != '0':
                        self.y = (i + 1) * 40
                        self.Vy = 0
                        # self.Vy = max(self.Vy, 0)
