import pygame
from Falling_blocks import *
from Menu import *
from pygame import time, draw

import pygame as pg
import keyboard
from Falling_blocks import *
from level_constructor import *

my_time = 0
surf_wasted = pygame.Surface((1200, 600))
surf_wasted.set_alpha(20)

max_HP1 = 240

max_HP2 = 240
w = 0
FPS = 60
clock = pg.time.Clock()
prozrachost = 0


class Personage:
    def __init__(self, screen, num):
        '''
        self.x координата левого вверхнего угла по горизонтали
        self.y - координата левого вверхнего угла по вертикали
        self.radius - костыль для упррощения, потому что сейчас персонаж это шарик.
        self.width - ширина персонажа, для нормальной отрисовки и проверки касаний собъектами.
        Считается от левого вверхнего угла
        self.height - высота персонажа для проверки касаний. Считается от левого вверхнего угла
        :param screen: экран, на который выводится персонаж
        self.died - показатель смерти. 0-жив, 1-мертв(от взрыва),2-ни жив, ни мертв, 3-умерла из-за времени
        (если будете добавлять другие источники смерти,то обозначайте их другими цифрами, чтобы разделять анимаwии)
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
        self.img = pg.image.load('графика/girl0.png').convert_alpha()
        self.img_left = pg.image.load('графика/girl_left2.png').convert_alpha()
        self.img2 = pg.image.load('графика/2_pers0.png').convert_alpha()
        self.img_left2 = pg.image.load('графика/2_pers_left0.png').convert_alpha()
        self.block_jump_speed = 23
        self.died1 = 0
        self.died2 = 0
        self.surf_wasted_img1 = pygame.image.load('графика/wasted1.png').convert_alpha()
        self.surf_wasted_img2 = pygame.image.load('графика/wasted2.png').convert_alpha()
        self.surf_wasted_draw = pygame.image.load('графика/draw.png').convert_alpha()

        self.power_up = 15
        self.time_after_up = 0
        self.bar1 = pg.image.load('графика/голова.png').convert_alpha()
        self.bar2 = pg.image.load('графика/bar2.png').convert_alpha()
        self.num = num
        self.Hp1 = 240
        self.Hp2 = 240

    def HP1(self):
        '''
        показатель жизней. уменьшается при стоянии
        '''

        if self.Vx == 0:
            self.Hp1 -= 0.6
        else:
            if 0 < self.Vx <= 1:
                self.Hp1 += 1.1
            if 0 > self.Vx >= -1:
                self.Hp1 += 1.1
            if self.Vx > 0 and self.Vx > 1:
                self.Hp1 += 1.1 * self.Vx
            if self.Vx < 0 and self.Vx < (-1):
                self.Hp1 += 1.1 * (-self.Vx)
        if self.Hp1 > max_HP1:
            self.Hp1 = max_HP1
        if self.Hp1 < 0:
            self.died1 = 3
        self.screen.blit(self.bar1, (25, 500))

    def draw_HP1(self):
        '''
        рисуем жизни
        '''
        rect(self.screen, (120, 100, 255), (118, 530, self.Hp1 // 1.87, 40))

    def HP2(self):
        '''
        показатель жизней. уменьшается при стоянии
        '''
        if self.Vx == 0:
            self.Hp2 -= 0.6
        else:
            if 0 < self.Vx <= 1:
                self.Hp2 += 1.1
            if 0 > self.Vx >= -1:
                self.Hp2 += 1.1
            if self.Vx > 0 and self.Vx > 1:
                self.Hp2 += 1.1 * self.Vx
            if self.Vx < 0 and self.Vx < (-1):
                self.Hp2 += 1.1 * (-self.Vx)
        if self.Hp2 > max_HP2:
            self.Hp2 = max_HP2
        if self.Hp2 < 0:
            self.died2 = 3

        # print(HP2)
        self.screen.blit(self.bar2, (1200 - 255, 500))

    def draw_HP2(self):
        '''
        рисуем жизни
        '''
        rect(self.screen, (200, 100, 200), (1200 - 118 - self.Hp2 // 1.87, 530, self.Hp2 // 1.87, 40))

    def move_personage(self, map, Painting):
        g = 0.3
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
                self.Vy = -5
                self.onGround = False
                self.time_after_up += 1

        if self.Vy >= 0:
            self.time_after_up = 0

        if keyboard.is_pressed('a') and -5 <= self.Vx <= 5:
            self.Vx -= self.acceleration
            self.direction = True
        if keyboard.is_pressed('d') and -5 <= self.Vx <= 5:
            self.Vx += self.acceleration
            self.direction = False

        if self.Vx > 0 and (not keyboard.is_pressed('d')):
            self.Vx -= 2 * self.acceleration
            if -0.5 <= self.Vx <= 0.5:
                self.Vx = 0

        if self.Vx < 0 and (not keyboard.is_pressed('a')):
            self.Vx += 2 * self.acceleration
            if -0.5 <= self.Vx <= 0.5:
                self.Vx = 0

        self.y += self.Vy
        if not self.onGround:
            self.Vy += g
        self.onGround = False
        self.Collision_y(map, Painting)

        self.x += self.Vx
        self.Collision_x(map, Painting)

        self.Collision_with_death_block(map)
        self.Collision_with_finish_block(map)

        return 0

    def draw_animations(self):
        global w, my_time, prozrachost
        death_screen = True
        death_menu = Menu()
        retry_but = Retry_but(WIDTH / 2 - 50, 450, 100, 50, "pic1.png", "Retry", "Retry")
        back_but = Back_to_menu_but(WIDTH / 2 - 50, 520, 100, 50, "pic1.png", "Back to menu", "Back_to_menu")
        death_menu.put_button(retry_but)
        death_menu.put_button(back_but)
        running = False
        map_chosen = False
        menu_opened = False
        while death_screen:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    death_screen = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    for butt in death_menu.buttons:
                        if butt.x <= event.pos[0] <= butt.x + butt.length and butt.y <= event.pos[1] <= butt.y + butt.width:
                            if butt.name == "Retry":
                                running = True
                                map_chosen = True
                                menu_opened = False
                                death_screen = False
                                self.died1 = 0
                            else:
                                running = True
                                map_chosen = False
                                menu_opened = True
                                death_screen = False
                                self.died1 = 0
            '''отрисовка конечной заставки'''
            my_time += 1
            clock.tick(30)
            self.screen.blit(surf_wasted, (0, 0))
            for butt in death_menu.buttons:
                butt.draw(self.screen)
            pg.display.update()

            if my_time >= 25:
                self.surf_wasted_img2.set_alpha(prozrachost)
                self.screen.blit(self.surf_wasted_draw, (456, 230))
                pg.display.update()
                clock.tick(30)
                prozrachost += 8

    def death_animations1(self):
        '''
        Анимации смертей. Два типа:со взрывом и без него
        '''

        global w, my_time, prozrachost
        death_screen = True
        death_menu = Menu()
        retry_but = Retry_but(WIDTH / 2 - 50, 450, 100, 50, "pic1.png", "Retry", "Retry")
        back_but = Back_to_menu_but(WIDTH / 2 - 50, 520, 100, 50, "pic1.png", "Back to menu", "Back_to_menu")
        death_menu.put_button(retry_but)
        death_menu.put_button(back_but)
        running = False
        map_chosen = False
        menu_opened = False
        if self.died1 != 3:
            death_screen = True
            animation_set_explosion = [pygame.image.load(f"графика/explosion{w}.png").convert_alpha() for w in
                                       range(0, 8)]
            for i in range(6):
                self.screen.blit(animation_set_explosion[i], (int(self.x), int(self.y)))
                clock.tick(8)
                pg.display.update()
            while death_screen:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        death_screen = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        for butt in death_menu.buttons:
                            if butt.x <= event.pos[0] <= butt.x + butt.length and butt.y <= event.pos[1] <= butt.y + butt.width:
                                if butt.name == "Retry":
                                    running = True
                                    map_chosen = True
                                    menu_opened = False
                                    death_screen = False
                                    self.died1 = 0
                                else:
                                    running = True
                                    map_chosen = False
                                    menu_opened = True
                                    death_screen = False
                                    self.died1 = 0
                '''отрисовка конечной заставки'''
                my_time += 1
                clock.tick(30)
                self.screen.blit(surf_wasted, (0, 0))
                for butt in death_menu.buttons:
                    butt.draw(self.screen)
                pg.display.update()

                if my_time >= 25:
                    self.surf_wasted_img2.set_alpha(prozrachost)
                    self.screen.blit(self.surf_wasted_img2, (456, 230))
                    pg.display.update()
                    clock.tick(30)
                    prozrachost += 8
        else:
            death_screen = True
            while death_screen:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        death_screen = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        for butt in death_menu.buttons:
                            if butt.x <= event.pos[0] <= butt.x + butt.length and butt.y <= event.pos[1] <= butt.y + butt.width:
                                if butt.name == "Retry":
                                    running = True
                                    map_chosen = True
                                    menu_opened = False
                                    death_screen = False
                                    self.died1 = 0
                                else:
                                    running = True
                                    map_chosen = False
                                    menu_opened = True
                                    death_screen = False
                                    self.died1 = 0
                my_time += 1
                clock.tick(30)
                self.screen.blit(surf_wasted, (0, 0))
                for butt in death_menu.buttons:
                    butt.draw(self.screen)
                pg.display.update()

                if my_time >= 25:
                    self.surf_wasted_img2.set_alpha(prozrachost)
                    self.screen.blit(self.surf_wasted_img2, (456, 230))
                    pg.display.update()
                    clock.tick(30)
                    prozrachost += 8
        return running, map_chosen, menu_opened

    def death_animations2(self):
        '''
        Анимации смертей. Два типа:со взрывом и без него
        '''
        global w, my_time, prozrachost
        self.Hp2 = 240
        death_screen = True
        death_menu = Menu()
        retry_but = Retry_but(WIDTH / 2 - 50, 450, 100, 50, "pic1.png", "Retry", "Retry")
        back_but = Back_to_menu_but(WIDTH / 2 - 50, 520, 200, 50, "pic1.png", "Back to menu", "Back_to_menu")
        death_menu.put_button(retry_but)
        death_menu.put_button(back_but)
        running = False
        map_chosen = False
        menu_opened = False
        if self.died2 != 3:
            death_screen = True
            animation_set_explosion = [pygame.image.load(f"графика/explosion{w}.png").convert_alpha() for w in
                                       range(0, 8)]
            for i in range(6):
                self.screen.blit(animation_set_explosion[i], (int(self.x), int(self.y)))
                clock.tick(8)
                pg.display.update()
            while death_screen:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        death_screen = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        for butt in death_menu.buttons:
                            if butt.x <= event.pos[0] <= butt.x + butt.length and butt.y <= event.pos[1] <= butt.y + butt.width:
                                if butt.name == "Retry":
                                    running = True
                                    map_chosen = True
                                    menu_opened = False
                                    death_screen = False
                                    self.died2 = 0
                                else:
                                    running = True
                                    map_chosen = False
                                    menu_opened = True
                                    death_screen = False
                                    self.died2 = 0
                '''отрисовка конечной заставки'''
                my_time += 1
                clock.tick(30)
                self.screen.blit(surf_wasted, (0, 0))
                for butt in death_menu.buttons:
                    butt.draw(self.screen)
                pg.display.update()

                if my_time >= 25:
                    self.surf_wasted_img1.set_alpha(prozrachost)
                    self.screen.blit(self.surf_wasted_img1, (456, 230))
                    pg.display.update()
                    clock.tick(30)
                    prozrachost += 8
        else:
            death_screen = True
            while death_screen:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        death_screen = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        for butt in death_menu.buttons:
                            if butt.x <= event.pos[0] <= butt.x + butt.length and butt.y <= event.pos[1] <= butt.y + butt.width:
                                if butt.name == "Retry":
                                    running = True
                                    map_chosen = True
                                    menu_opened = False
                                    death_screen = False
                                    self.died2 = 0
                                else:
                                    running = True
                                    map_chosen = False
                                    menu_opened = True
                                    death_screen = False
                                    self.died2 = 0
                my_time += 1
                clock.tick(30)
                self.screen.blit(surf_wasted, (0, 0))
                for butt in death_menu.buttons:
                    butt.draw(self.screen)
                pg.display.update()

                if my_time >= 25:
                    self.surf_wasted_img1.set_alpha(prozrachost)
                    self.screen.blit(self.surf_wasted_img1, (456, 230))
                    pg.display.update()
                    clock.tick(30)
                    prozrachost += 8
        return running, map_chosen, menu_opened

    def collusion_with_red_block1(self, raw_listik):
        '''
        Функция проверяет пересечение Кима и персонажа для 1го перса
        '''
        for raw in raw_listik:
            if (raw.y - 20) < self.y < (raw.y + 30) or raw.y < (self.y + 45) < (raw.y + 40):
                for i in range(len(raw.block_pos)):
                    if raw.block_pos[i] == 0:
                        if i * 40 < (self.x + 30) < (i * 40 + 40):
                            # print(Huuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuy')
                            if self.died1 == 0:
                                self.died1 = 1

    def collusion_with_red_block2(self, raw_listik):
        '''
        Функция проверяет пересечение Кима и персонажа для 2го перса
        '''
        for raw in raw_listik:
            if (raw.y - 20) < self.y < (raw.y + 30) or raw.y < (self.y + 45) < (raw.y + 40):
                for i in range(len(raw.block_pos)):
                    if raw.block_pos[i] == 0:
                        if i * 40 < (self.x + 30) < (i * 40 + 40):
                            # print(Huuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuy')
                            if self.died2 == 0:
                                self.died2 = 1

    def move_personage_2(self, map, Painting):
        g = 0.3
        if self.Vy < 0 or self.onGround:
            if keyboard.is_pressed('up_arrow') and self.time_after_up < 20:
                self.Vy = -5
                self.onGround = False
                self.time_after_up += 1

        if self.Vy >= 0:
            self.time_after_up = 0

        if keyboard.is_pressed('left_arrow') and -5 <= self.Vx <= 5:
            self.Vx -= self.acceleration
            self.direction = True
        if keyboard.is_pressed('right_arrow') and -5 <= self.Vx <= 5:
            self.Vx += self.acceleration
            self.direction = False

        if self.Vx > 0 and (not keyboard.is_pressed('right_arrow')):
            self.Vx -= 2 * self.acceleration
            if -0.5 <= self.Vx <= 0.5:
                self.Vx = 0

        if self.Vx < 0 and (not keyboard.is_pressed('left_arrow')):
            self.Vx += 2 * self.acceleration
            if -0.5 <= self.Vx <= 0.5:
                self.Vx = 0

        self.y += self.Vy
        if not self.onGround:
            self.Vy += g
        self.onGround = False
        self.Collision_y(map, Painting)

        self.x += self.Vx
        self.Collision_x(map, Painting)

        self.Collision_with_death_block(map)
        self.Collision_with_finish_block(map)

        return 0

    def Personage_animation_moveemnt(self, block, mapik, max_pers_x):
        '''
        анимация бега вправо и лево, стояния на месте
        '''
        global w
        animation_set = [pygame.image.load(f"графика/girl{w}.png").convert_alpha() for w in range(0, 9)]
        animation_set_left = [pygame.image.load(f"графика/girl_left{w}.png").convert_alpha() for w in range(0, 9)]
        if self.Vx > 0:
            if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:

                    self.screen.blit(animation_set[w], (WIDTH / 2, int(self.y)))
                else:

                    self.screen.blit(animation_set[w], (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(animation_set[w], (int(self.x), int(self.y)))

            else:

                self.screen.blit(animation_set[w],
                                 (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        if self.Vx < 0:
            if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:

                    self.screen.blit(animation_set_left[w], (WIDTH / 2, int(self.y)))
                else:

                    self.screen.blit(animation_set_left[w], (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(animation_set_left[w], (int(self.x), int(self.y)))
            else:

                self.screen.blit(animation_set_left[w],
                                 (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        if self.Vx == 0:
            if self.direction:
                if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    if self.x == max_pers_x:

                        self.screen.blit(self.img_left, (WIDTH / 2, int(self.y)))
                    else:

                        self.screen.blit(self.img_left, (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
                elif max_pers_x < WIDTH / 2:

                    self.screen.blit(self.img_left, (int(self.x), int(self.y)))
                else:

                    self.screen.blit(self.img_left,
                                     (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

            else:
                if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    if self.x == max_pers_x:

                        self.screen.blit(self.img, (WIDTH / 2, int(self.y)))
                    else:

                        self.screen.blit(self.img, (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
                elif max_pers_x < WIDTH / 2:

                    self.screen.blit(self.img, (int(self.x), int(self.y)))
                else:
                    self.screen.blit(self.img,
                                     (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

    def Personage_animation_moveemnt2(self, block, mapik, max_pers_x):
        '''
        анимация бега вправо и лево, стояния на месте
        '''
        global w
        animation_set2 = [pygame.image.load(f"графика/2_pers{w}.png").convert_alpha() for w in range(0, 8)]
        animation_set_left2 = [pygame.image.load(f"графика/2_pers_left{w}.png").convert_alpha() for w in range(0, 8)]
        if self.Vx > 0:
            if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:

                    self.screen.blit(animation_set2[w], (WIDTH / 2, int(self.y)))
                else:

                    self.screen.blit(animation_set2[w], (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(animation_set2[w], (int(self.x), int(self.y)))

            else:

                self.screen.blit(animation_set2[w],
                                 (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        if self.Vx < 0:
            if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:

                    self.screen.blit(animation_set_left2[w], (WIDTH / 2, int(self.y)))
                else:

                    self.screen.blit(animation_set_left2[w], (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(animation_set_left2[w], (int(self.x), int(self.y)))
            else:

                self.screen.blit(animation_set_left2[w],
                                 (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        if self.Vx == 0:
            if self.direction:
                if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    if self.x == max_pers_x:

                        self.screen.blit(self.img_left2, (WIDTH / 2, int(self.y)))
                    else:

                        self.screen.blit(self.img_left2, (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
                elif max_pers_x < WIDTH / 2:

                    self.screen.blit(self.img_left2, (int(self.x), int(self.y)))
                else:

                    self.screen.blit(self.img_left2,
                                     (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

            else:
                if WIDTH / 2 <= max_pers_x <= len(mapik.map_list[0]) * block.length - WIDTH / 2:
                    if self.x == max_pers_x:

                        self.screen.blit(self.img2, (WIDTH / 2, int(self.y)))
                    else:

                        self.screen.blit(self.img2, (WIDTH / 2 - max_pers_x + self.x, int(self.y)))
                elif max_pers_x < WIDTH / 2:

                    self.screen.blit(self.img2, (int(self.x), int(self.y)))
                else:
                    self.screen.blit(self.img2,
                                     (- len(mapik.map_list[0]) * block.length + self.x + WIDTH, int(self.y)))

        w += 1
        if w == 8:
            w = 0

        w += 1
        if w == 8:
            w = 0

    def Collision_with_death_block(self, map):
        for j in range(int(self.x + 22) // 40, (int(self.x) + self.width - 22) // 40 + 1):
            for i in range(int(self.y - 1) // 40, (int(self.y) + self.height + 1) // 40 + 1):
                if map[i][j] == '5':
                    if self.num == 1:
                        self.died1 = 3
                    else:
                        self.died2 = 3
        for j in range(int(self.x + 2) // 40, (int(self.x) + self.width - 2) // 40 + 1):
            for i in range(int(self.y + 10) // 40, (int(self.y) + self.height - 10) // 40 + 1):
                if map[i][j] == '5':
                    if self.num == 1:
                        self.died1 = 3
                    else:
                        self.died2 = 3

    def Collision_with_finish_block(self, map):
        for j in range(int(self.x + 22) // 40, (int(self.x) + self.width - 22) // 40 + 1):
            for i in range(int(self.y - 1) // 40, (int(self.y) + self.height + 1) // 40 + 1):
                if map[i][j] == '3':
                    if self.num == 2:
                        self.died1 = 3
                    else:
                        self.died2 = 3
        for j in range(int(self.x + 2) // 40, (int(self.x) + self.width - 2) // 40 + 1):
            for i in range(int(self.y + 10) // 40, (int(self.y) + self.height - 10) // 40 + 1):
                if map[i][j] == '3':
                    if self.num == 2:
                        self.died1 = 3
                    else:
                        self.died2 = 3

    def Collision_x(self, map, Painting):
        '''
        функция проверяет касание с блоками по x и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        if self.Vx > 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40 + 1):
                for i in range(int(self.y + 1) // 40, (int(self.y - 1) + self.height) // 40 + 1):
                    if map[i][j] not in ["0", "5", "3", "8", "9", "10"]:
                        self.x = j * 40 - self.width
                        if Painting:
                            if self.num == 1:
                                map[i][j] = '6'
                            else:
                                map[i][j] = '7'

        if self.Vx < 0:
            for j in range(int(self.x) // 40, (int(self.x) + self.width) // 40):
                for i in range(int(self.y + 1) // 40, (int(self.y - 1) + self.height) // 40 + 1):
                    if map[i][j] not in ["0", "5", "3", "8", "9", "10"]:
                        self.x = (j + 1) * 40
                        if Painting:
                            if self.num == 1:
                                map[i][j] = '6'
                            else:
                                map[i][j] = '7'

    def Collision_y(self, map, Painting):
        '''
        функция проверяет касание с блоками по y и выталкивает при касании
        :param map: карта текущая
        :return: ничего не выводит, только двигает
        '''
        if self.Vy > 0:
            for j in range(int(self.x + 1) // 40, (int(self.x - 1) + self.width) // 40 + 1):
                for i in range(int(self.y) // 40, (int(self.y) + self.height) // 40 + 1):
                    if map[i][j] not in ["0", "5", "3", "8", "9", "10"]:
                        self.y = i * 40 - self.height
                        self.onGround = True
                        if Painting:
                            if self.num == 1:
                                map[i][j] = '6'
                            else:
                                map[i][j] = '7'
                    if map[i][j] == '4':
                        self.Vy -= self.block_jump_speed

        if self.Vy < 0:
            for j in range(int(self.x + 1) // 40, (int(self.x - 1) + self.width) // 40 + 1):
                for i in range(int(self.y) // 40, (int(self.y) + self.height - 1) // 40 + 1):
                    if map[i][j] not in ["0", "5", "3", "8", "9", "10"]:
                        self.y = (i + 1) * 40
                        self.Vy = 0
                        if Painting:
                            if self.num == 1:
                                map[i][j] = '6'
                            else:
                                map[i][j] = '7'
