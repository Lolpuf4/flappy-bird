import pygame as pg
import random
import settings


class Tubes:
    def __init__(self, game, hole_size):
        self.game = game
        self.size = random.randint(300, 600)
        self.hole_size = hole_size
        self.image = pg.image.load("PipeStyle1.png")
        self.pic1 = self.image.subsurface(0, 0, 32, 80).copy()
        self.pic1 = pg.transform.scale(self.pic1, [self.pic1.get_width() * 5, self.size])
        self.pic1_bottom = pg.transform.scale(self.pic1, [self.pic1.get_width(), settings.SCREEN_HEIGHT - self.size - int(self.hole_size)])
        self.speed = 10
        self.scored = False


        self.hitbox_top = pg.Rect([settings.SCREEN_WIDTH, 0], [self.pic1.get_width(), self.size])
        self.hitbox_bottom = pg.Rect([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT - (settings.SCREEN_HEIGHT - self.hitbox_top.height - int(self.hole_size))], [self.pic1.get_width(), settings.SCREEN_HEIGHT])

    def update(self):
        self.hitbox_top.x -= int(self.speed)
        self.hitbox_bottom.x -= int(self.speed)

        self.speed = self.game.tubes[0].speed
        self.game.hole_size -= 0.1

        self.speed += 0.02

    def draw(self):

        self.game.screen.blit(self.pic1, self.hitbox_top)
        self.game.screen.blit(self.pic1_bottom, self.hitbox_bottom)
