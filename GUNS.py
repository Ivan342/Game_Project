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

    def draw_gun(self):
        if  not self.napr:
            self.screen.blit(self.img_right, (int(self.x), int(self.y)))
        else:
            self.screen.blit(self.img_left, (int(self.x), int(self.y)))

    def move_gun(self):
        self.napr = self.pers.direction

        #print(self.napr)
        if not self.napr:
            self.x = self.pers.x + self.pers.width * 0.35
            self.y = self.pers.y + self.pers.height / 2
        if self.napr:
            self.x = self.pers.x - self.width + self.pers.width * 0.75
            self.y = self.pers.y + self.pers.height / 2