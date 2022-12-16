import pygame as pg
from pygame import time
from pygame.draw import *
from Personage import *
from bullet import *
from level_constructor import *
from Falling_blocks import *
from Menu import *
from GUNS import *
import time as TIME
from math import *

WIDTH = 1200
HEIGHT = 600

pg.mixer.init()


FPS = 60
clock = pg.time.Clock()
time_scale = 1000
pg.init()
WIDTH = 1200
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
running = True
block = Block(screen)
pers = Personage(screen, 1)
pers_2 = Personage(screen, 2)
menu = Menu()
exit_button = Exit_button(980, 230, 100, 50, "pic1.png", "Exit", "Exit")
fal_block_lvl_but = Fal_blocks_lvl_but(980, 10, 250, 50, "pic1.png", "Falling blocks", "F_b_lvl")
racing_lvl_but = Racing_lvl_but(980, 80, 250, 50, "pic1.png", "Racing", "Racing_lvl")
color_battle_lvl_but = Color_battle_lvl_but(980, 150, 250, 50, "pic1.png", "Color battle", "Color_battle_lvl")
menu.put_button(fal_block_lvl_but)
menu.put_button(racing_lvl_but)
menu.put_button(color_battle_lvl_but)
menu.put_button(exit_button)
map = MAP()
'''
Здесь создаем карту как объект отдельного класса карт, чтобы к нему можно было обращаться из любой программы.
Класс прописан level_constructor
'''

pg.mixer.music.load('звуки/music_menu.wav')
pg.mixer.music.play(-1)
flag_start = False
'''
Тут делается фоновая музыка. 
flag_start показывает, что игра перешла от меню, к игре
'''

sound_fire = pg.mixer.Sound('звуки/fire.wav')
sound_uwu = pg.mixer.Sound('звуки/uwu_final.wav')
'''Это звуки когда девочка умирает'''

sound_shoot = pg.mixer.Sound('звуки/shoot.wav')
'''Звук выстрела'''


fall_raw = Fall_block_raw(screen)
spawn_filled = False
need_clean = False
level_chosen = False
flag = False
game_speed = 1
start_time = time.get_ticks()
field = pg.image.load('графика/фон1.jpg').convert()
gun = GUN(screen, pers)
gun_2 = GUN(screen, pers_2)
t = 0
t_2 = 0

bullets = []
bullets_2 = []
color_time = 1200

while running:

    while menu_opened:
        menu.draw_menu(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu_opened = False
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                for butt in menu.buttons:
                    if butt.x <= event.pos[0] <= butt.x + butt.length and butt.y <= event.pos[1] <= butt.y + butt.width:
                        if butt.name == "Exit":
                            running = False
                        elif butt.name == "F_b_lvl":
                            map.map_list = []
                            map.read_map(butt.push_me())
                            level_chosen = True
                            Kim = True
                            Color = False
                            pers = Personage(screen, 1)
                            pers_2 = Personage(screen, 2)
                            gun = GUN(screen, pers)
                            gun_2 = GUN(screen, pers_2)
                            gun.draw_gun(block, map.map_list, max(pers.x, pers_2.x) )
                            gun_2.draw_gun(block, map.map_list, max(pers.x, pers_2.x) )
                        elif butt.name == "Racing_lvl":
                            map.map_list = []
                            map.read_map(butt.push_me())
                            level_chosen = True
                            Kim = False
                            Color = False
                        else:
                            map.map_list = []
                            map.read_map(butt.push_me())
                            level_chosen = True
                            Kim = False
                            Color = True
                            color_time = 1200
                        menu_opened = False

        pg.display.update()

    if not flag_start:
        pg.mixer.music.stop()
        pg.mixer.music.load('звуки/music_game.wav')
        pg.mixer.music.play(-1)
        flag_start = True

    if level_chosen:
        if Color:
            color_time -= 1
            #print(color_time)
            if color_time == 0:
                str_map_list = str(map.map_list)
                if str_map_list.count('6') > str_map_list.count('7'):
                    pers_2.died2 = 3
                else:
                    pers.died1 = 3
                color_time = 1200

        screen.blit(field, (0, 0))
        if Kim:
            gun.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            gun_2.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            for raw in fall_raw.raw_list:
                raw.fall()
                raw.draw()
                if raw.y > HEIGHT + raw.length:
                    need_clean = True
                if fall_raw.raw_list[-1].y <= -raw.length + 100 + raw.length:
                    spawn_filled = True

                else:
                    spawn_filled = False

            if not spawn_filled:
                fall_raw.new_raw(screen, game_speed)
                spawn_filled = True
            if need_clean:
                raw.clear()
                need_clean = False

            game_speed += fall_raw.raw_list[0].accel
        map.map_chase(block, max(pers.x, pers_2.x))

        # map.map_chase(block, pers_2.x)
        # pers.draw()

        '''
        (если будете добавлять другие источники смерти,
        то обозначайте их другими цифрами, чтобы разделять анимаwии)
        '''
        if pers.died1 == 0:
            '''
            жизнь 1го перса
            '''
            pers.collusion_with_red_block1(fall_raw.raw_list)
            pers.move_personage(map.map_list, Color)
            pers.Personage_animation_moveemnt(block, map, max(pers.x, pers_2.x))
            pers.collusion_with_red_block1(fall_raw.raw_list)
            pers.draw_HP1()
            pers.HP1()
            if Kim:
                gun.move_gun()
                gun.draw_gun(block, map.map_list, max(pers.x, pers_2.x))

        if pers_2.died2 == 0:
            '''
            Жизнь 2го перса
            '''
            pers_2.collusion_with_red_block2(fall_raw.raw_list)
            pers_2.move_personage_2(map.map_list, Color)
            pers_2.Personage_animation_moveemnt2(block, map, max(pers.x, pers_2.x))
            pers_2.collusion_with_red_block2(fall_raw.raw_list)
            pers_2.draw_HP2()
            pers_2.HP2()
            if Kim:
                gun_2.move_gun()
                gun_2.draw_gun(block, map.map_list, max(pers.x, pers_2.x))

        if pers.died1 == 1:
            '''
            смерть 1го перса
            '''
            sound_fire.play()
            running, map_chosen, menu_opened = pers.death_animations1()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)
            gun = GUN(screen, pers)
            gun_2 = GUN(screen, pers_2)
            gun.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            gun_2.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            map.map_list = []

            if Kim:
                fall_raw.raw_list = []
                fall_raw.new_raw(screen, game_speed)
                spawn_filled = False
                map.read_map(fal_block_lvl_but.push_me())
            elif Color:
                color_time = 1200
                map.read_map(color_battle_lvl_but.push_me())
            else:
                map.read_map(racing_lvl_but.push_me())

            game_speed = 1

        if (pers.died1 == 3) or (pers_2.died1 == 3):
            sound_uwu.play()

            running, map_chosen, menu_opened = pers.death_animations1()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)

            gun = GUN(screen, pers)
            gun_2 = GUN(screen, pers_2)
            gun.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            gun_2.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            map.map_list = []
            if Kim:
                fall_raw.raw_list = []
                fall_raw.new_raw(screen, game_speed)
                spawn_filled = False
                map.read_map(fal_block_lvl_but.push_me())
            elif Color:
                color_time = 1200
                map.read_map(color_battle_lvl_but.push_me())
            else:
                map.read_map(racing_lvl_but.push_me())
            game_speed = 1

        if pers_2.died2 == 1:
            '''
            Смерть 2го перса
            '''
            sound_fire.play()
            running, map_chosen, menu_opened = pers_2.death_animations2()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)
            gun = GUN(screen, pers)
            gun_2 = GUN(screen, pers_2)
            gun.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            gun_2.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            map.map_list = []
            if Kim:
                fall_raw.raw_list = []
                fall_raw.new_raw(screen, game_speed)
                spawn_filled = False
                map.read_map(fal_block_lvl_but.push_me())
            elif Color:
                color_time = 1200
                map.read_map(color_battle_lvl_but.push_me())
            else:
                map.read_map(racing_lvl_but.push_me())
            game_speed = 1

        if (pers_2.died2 == 3) or (pers.died2 == 3):
            sound_uwu.play()
            running, map_chosen, menu_opened = pers_2.death_animations2()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)
            gun = GUN(screen, pers)
            gun_2 = GUN(screen, pers_2)
            gun.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            gun_2.draw_gun(block, map.map_list, max(pers.x, pers_2.x))
            map.map_list = []
            if Kim:
                fall_raw.raw_list = []
                fall_raw.new_raw(screen, game_speed)
                spawn_filled = False
                map.read_map(fal_block_lvl_but.push_me())
            elif Color:
                color_time = 1200
                map.read_map(color_battle_lvl_but.push_me())
            else:
                map.read_map(racing_lvl_but.push_me())
            game_speed = 1

        # pers_2.move_personage_2(map.map_list)
        # pers_2.Personage_animation_move_right(block, map)
        # pers.move_personage(map)

        dt = time.get_ticks() - start_time

        if TIME.time() - t >= 1:
            if keyboard.is_pressed('q') and Kim:
                bullet = Bullet(screen, gun, pers)
                bullets.append(bullet)
                t = TIME.time()
                sound_shoot.play()

        if TIME.time() - t_2 >= 1:
            if keyboard.is_pressed('m') and Kim:
                bullet = Bullet(screen, gun, pers_2)
                bullets.append(bullet)
                t_2 = TIME.time()
                sound_shoot.play()

        for i in bullets:
            i.move_bullet()
            i.draw_bullet()
            if i.collision(map.map_list):
                bullets.remove(i)

        for i in bullets:
            if (i.x >= pers.x and i.x <= pers.x + pers.width) and (i.y >= pers.y and i.y <= pers.y + pers.height):
                bullets.remove(i)
                pers.Vx += i.Vx
                pers.Vy += i.Vy

            if (i.x >= pers_2.x and i.x <= pers_2.x + pers_2.width) and (
                    i.y >= pers_2.y and i.y <= pers_2.y + pers_2.height):
                bullets.remove(i)
                pers_2.Vx += i.Vx
                pers_2.Vy += i.Vy

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        if Color:
            #rect(screen, (40, 120, 0), (500, 30, color_time // 8, 40))
            circle(screen, (20, 60, 0), (600, 80), 30)
            arc(screen, (180, 100, 80), (600-30, 80-30, 60, 60), 0, 2*pi*(color_time/1200), 5)
            #pie(screen, (40, 120, 0), (600, 80), 30, 0, (color_time/500)*360)

            pg.display.update()
        pg.display.update()
        clock.tick(FPS)
        (clock.get_time())
pg.quit()
