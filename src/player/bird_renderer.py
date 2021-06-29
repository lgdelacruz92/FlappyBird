import pygame
from utils.spritesheet import SpriteSheet


class BirdRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Global game object
        self.game = game

        # pygame
        self.pygame = game.pygame
        self.pygame.sprite.Sprite.__init__(self)

        # get global game scale
        self.rects = [
            (2, 490, 18, 14),
            (30, 490, 18, 14),
            (58, 490, 18, 14),
        ]

        #state
        self.flying = False

        # start images
        self.load_images()

        # get global game scren
        self.screen = game.screen
        self.ticks = 0
        self.flap = 0

    def load_images(self, bird=None):
        angle = 0
        if bird is not None:
            angle = bird.angle

        scale = self.game.config.scale
        # load the bird img
        self.bird_imgs = []
        for rect in self.rects:
            bird_img = self.game.spritesheet.image_at(rect, colorkey=-1)
            bird_img = self.game.pygame.transform.scale(
                bird_img,
                (int(bird_img.get_width() * scale), int(bird_img.get_height() * scale))
            )
            bird_img = self.game.pygame.transform.rotate(bird_img, angle)
            self.bird_imgs.append(bird_img)

    def draw_flying(self, bird):
        num_imgs = len(self.bird_imgs)
        if self.game.config.frame_rate == self.ticks:
            self.ticks = 0
        if self.ticks % 5 == 0 and self.flying:
            self.flap += 1
            self.flap %= num_imgs
        else:
            self.flap = 0
        self.ticks += 1
        bird_img = self.bird_imgs[self.flap]
        rect = bird_img.get_rect()
        new_rect = (bird.x, bird.y, rect.width, rect.height)
        self.screen.blit(bird_img, new_rect)

    def draw(self, bird):
        if bird.v < 0:
            self.load_images(bird)
        else:
            self.load_images(bird)

        self.draw_flying(bird)
