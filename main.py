import pygame as pg
import pygame.freetype
import settings
import bird
import road
import tubes
pg.init()
class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.background = pg.image.load("Background1.png")
        self.background = pg.transform.scale(self.background, [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        self.started = False
        self.loss = False
        self.hole_size = 400
        self.score = 0

        self.clock = pg.time.Clock()

        self.tubes = [tubes.Tubes(self, self.hole_size)]
        self.bird = bird.Bird(self)

        self.text = pg.freetype.Font(None, 40)


        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(settings.FPS)

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and self.started and not self.loss:
                    self.bird.move()
                if event.key == pg.K_SPACE and not self.started and not self.loss:
                    self.started = True
                    self.bird.falling = True
                    self.bird.move()

                if event.key == pg.K_SPACE and self.loss:
                    self.hole_size = 400
                    self.tubes = [tubes.Tubes(self, self.hole_size)]
                    self.bird = bird.Bird(self)
                    self.started = False
                    self.loss = False
                    self.score = 0

    def update(self):
        for tube in self.tubes:
            if not self.loss and self.started:
                tube.update()

            if self.bird.hitbox.colliderect(tube.hitbox_top) or self.bird.hitbox.colliderect(tube.hitbox_bottom):
                self.started = False
                self.loss = True

            if self.bird.hitbox.x >= tube.hitbox_top.x and not tube.scored:
                self.score += 1
                tube.scored = True

        if self.started and not self.loss:
            self.bird.update()

        if self.bird.hitbox.bottom >= 1200:
            self.loss = True

        if self.tubes[-1].hitbox_top.x <= 1300:
            add_tube = tubes.Tubes(self, self.hole_size)
            self.tubes.append(add_tube)



    def draw(self):
        self.screen.blit(self.background, [0, 0])
        self.text.render_to(self.screen, [0, 0], str(self.score))
        for tube in self.tubes:
            tube.draw()
        self.bird.draw()

        pg.display.flip()

if __name__ == "__main__":
    Game()