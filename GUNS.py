from Personage import *


class GUN():
    def __init__(self, screen, pers):
        '''
        считается self.x от середины персонажа
        self.y тоже считается от середины персонажа
        self.Vy и self.Vx просто приравниваются к соответствующим скоростям персонажа
        но отрисовка просто следует за персонажем
        self.napr показывает, куда смотрит девочка
        '''
        self.width = 64
        self.screen = screen
        self.height = 20
        self.pers = pers
        self.x = self.pers.x + self.pers.width / 2
        self.y = self.pers.y + self.pers.height / 2
        self.Vy = pers.Vy
        self.Vx = pers.Vx
        self.img_right = pg.image.load('girl_new_right.png').convert_alpha()
        self.img_left = pg.image.load('girl_new_left.png').convert_alpha()
        self.napr = False

    def draw_gun(self, block, mapik, max_pers_x):
        self.x = self.pers.x
        self.y = self.pers.y
        self.napr = self.pers.direction
        if not self.napr:
            if max_pers_x >= WIDTH / 2 and max_pers_x <= len(mapik[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:

                    self.screen.blit(self.img_right,
                                     (WIDTH / 2 + self.pers.width * 0.6, int(self.y + self.pers.height / 2)))
                else:

                    self.screen.blit(self.img_right, (
                        WIDTH / 2 - max_pers_x + self.x + self.pers.width * 0.6, int(self.y + self.pers.height / 2)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(self.img_right,
                                 (int(self.x + self.pers.width * 0.6), int(self.y + self.pers.height / 2)))

            else:

                self.screen.blit(self.img_right,
                                 (- len(mapik[0]) * block.length + self.x + WIDTH + int(self.pers.width * 0.6),
                                  int(self.y + self.pers.height / 2)))

        if self.napr:
            if max_pers_x >= WIDTH / 2 and max_pers_x <= len(mapik[0]) * block.length - WIDTH / 2:
                if self.x == max_pers_x:

                    self.screen.blit(self.img_left, (
                        WIDTH / 2 + int(self.pers.width * 0.55 - self.width), int(self.y + self.pers.height / 2)))
                else:

                    self.screen.blit(self.img_left, (
                        WIDTH / 2 - max_pers_x + self.x + int(self.pers.width * 0.55 - self.width),
                        int(self.y + self.pers.height / 2)))
            elif max_pers_x < WIDTH / 2:

                self.screen.blit(self.img_left, (
                    int(self.x) + int(self.pers.width * 0.55 - self.width), int(self.y + self.pers.height / 2)))

            else:

                self.screen.blit(self.img_left,
                                 (- len(mapik[0]) * block.length + self.x + WIDTH + int(
                                     self.pers.width * 0.55 - self.width), int(self.y + self.pers.height / 2)))

    def move_gun(self):
        self.napr = self.pers.direction

        # print(self.napr)
        if not self.napr:
            self.x = self.pers.x + self.pers.width * 0.15
            self.y = self.pers.y + self.pers.height / 2
        if self.napr:
            self.x = self.pers.x - self.width + self.pers.width * 0.95
            self.y = self.pers.y + self.pers.height / 2
