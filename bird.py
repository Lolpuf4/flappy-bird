import pygame as pg
import settings

class Bird:
    def __init__(self, game):
        self.game = game

        self.images = []
        self.image_right_now = 0
        croping_cords = 0
        for pic in range(4):
            self.images.append(pg.transform.scale((pg.image.load("Bird1-1.png")).subsurface(croping_cords, 0 , 16, 16), [160, 160]))
            croping_cords += 16

        self.image = self.images[int(self.image_right_now)]

        self.hitbox = pg.Rect([settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2], self.images[0].get_size())
        self.falling = False
        self.rotate_image = 0
        self.rotate_angle = 45
        self.velocity_down = 10
        self.rotate_angle_down = 360

    def move(self):
        self.hitbox.y -= 100
        self.rotate_image = 5
        self.velocity_down = 10
        self.rotate_angle = 45
        self.rotate_angle_down = 360

    def update(self):
        self.hitbox.y += self.velocity_down
        self.velocity_down += 1
        if self.rotate_angle_down > 270:
            self.rotate_angle_down -= 3

    def draw(self):
        self.image = self.images[int(self.image_right_now)]
        if self.rotate_image:
            self.image = pg.transform.rotate(self.image, self.rotate_angle)
            self.rotate_image -= 1
        if self.falling:
            self.image = pg.transform.rotate(self.image, self.rotate_angle_down)
        self.game.screen.blit(self.image, self.hitbox)
        if not self.game.loss:
            self.image_right_now += 0.25
        if self.image_right_now >= len(self.images):
            self.image_right_now = 0
