import pygame as pg
from pygame import time
from pygame.draw import *
from Personage import *
from level_constructor import *
from Falling_blocks import *
from Menu import *
from GUNS import *

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

fall_raw = Fall_block_raw(screen)
spawn_filled = False
need_clean = False
level_chosen = False
game_speed = 1
start_time = time.get_ticks()
field = pg.image.load('фон1.jpg').convert()
gun = GUN(screen, pers)


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
                            map.read_map(butt.push_me())
                            level_chosen = True
                            Kim = True
                            Color = False
                        elif butt.name == "Racing_lvl":
                            map.read_map(butt.push_me())
                            level_chosen = True
                            Kim = False
                            Color = False
                        else:
                            map.read_map(butt.push_me())
                            level_chosen = True
                            Kim = False
                            Color = True
                        menu_opened = False

        pg.display.update()

    if level_chosen:

        screen.blit(field, (0, 0))
        if Kim:
            for raw in fall_raw.raw_list:
                raw.fall()
                raw.draw()
                if raw.y > HEIGHT + raw.length:
                    need_clean = True
                if fall_raw.raw_list[-1].y <= -raw.length + 100 + raw.length:
                    spawn_filled = True

                else:
                    spawn_filled = False
                    pass



        if not spawn_filled:
            fall_raw.new_raw(screen, game_speed)
            spawn_filled = True
        if need_clean:
            fall_raw.raw_list = raw.clear()
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
            pers.move_personage(map.map_list,Color)
            pers.Personage_animation_moveemnt(block, map, max(pers.x, pers_2.x))
            pers.collusion_with_red_block1(fall_raw.raw_list)
            pers.draw_HP1()
            pers.HP1()
            gun.move_gun()
            gun.draw_gun()
        if pers_2.died2 == 0:
            '''
            Жизнь 2го перса
            '''
            pers_2.collusion_with_red_block2(fall_raw.raw_list)
            pers_2.move_personage_2(map.map_list,Color)
            pers_2.Personage_animation_moveemnt(block, map, max(pers.x, pers_2.x))
            pers_2.collusion_with_red_block2(fall_raw.raw_list)
            pers_2.draw_HP2()
            pers_2.HP2()

        if pers.died1 == 1:
            '''
            смерть 1го перса
            '''
            running, map_chosen, menu_opened = pers.death_animations1()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)
            fall_raw.raw_list = []
            fall_raw.new_raw(screen, game_speed)

            game_speed = 1

        if pers.died1==3:
            running, map_chosen, menu_opened = pers.death_animations1()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)
            fall_raw.raw_list = []
            fall_raw.new_raw(screen, game_speed)
            spawn_filled = False
            game_speed = 1

        if pers_2.died2 == 1:
            '''
            Смерть 2го перса
            '''
            running, map_chosen, menu_opened = pers_2.death_animations2()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)
            fall_raw.raw_list = []
            fall_raw.new_raw(screen, game_speed)
            spawn_filled = False
            game_speed = 1
        if pers_2.died2==3:
            running, map_chosen, menu_opened = pers_2.death_animations2()
            pers = Personage(screen, 1)
            pers_2 = Personage(screen, 2)
            fall_raw.raw_list = []
            fall_raw.new_raw(screen, game_speed)
            spawn_filled = False
            game_speed = 1




    #pers_2.move_personage_2(map.map_list)
    #pers_2.Personage_animation_move_right(block, map)
    #pers.move_personage(map)



        dt = time.get_ticks() - start_time

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pers.x = event.pos[0]
                    pers.y = event.pos[1]

                    # pers_2.x = event.pos[0]
                    # pers_2.y = event.pos[1]
        pg.display.update()
        clock.tick(FPS)
        (clock.get_time())
pg.quit()


##