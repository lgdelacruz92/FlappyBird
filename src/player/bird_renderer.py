import pygame
from utils.spritesheet import SpriteSheet


class BirdRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Global game object
        self.game = game

        # pygame
        self.pygame = game.pygame
        self.pygame.sprite.Sprite.__init__(self)

        self.bird_rects = []
        for i in range(2, 5, 30):
            rect = (i, 490, 18, 14)
            self.bird_rects.append(rect)

        # get global game scale
        scale = game.config.scale

        # load the bird img
        self.bird_imgs = []
        for i in range(2, 5, 30):
            rect = (i, 490, 18, 14)
            bird_img = game.spritesheet.image_at(rect, colorkey=-1)
            bird_img = game.transform.scale(
                bird_img,
                (int(bird_img.get_width() * scale), int(bird_img.get_height() * scale))
            )
            self.bird_imgs.append(bird_img)

        # get global game scren
        self.screen = game.screen
        self.ticks = 0

    def draw_flying(self):
        self.screen.blit(self.bird, self.rect)

    def draw(self, bird):
        self.draw_flying()
