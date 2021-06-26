import pygame
from utils.spritesheet import SpriteSheet


class BirdRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Global game object
        self.game = game

        # pygame
        self.pygame = game.pygame
        self.pygame.sprite.Sprite.__init__(self)

        self.rect = (2, 490, 18, 14)

        # load the bird img
        flying_bird_img = game.config.flying_bird_url
        flying_img = game.spritesheet.image_at(self.rect, colorkey=-1)

        # get global game scale
        scale = game.config.scale

        # get global game scren
        self.screen = game.screen

        # add image
        self.bird = self.pygame.transform.scale(
            flying_img, (int(flying_img.get_width() * scale), int(flying_img.get_height() * scale)))

    def draw_flying(self):
        self.screen.blit(self.bird, self.rect)

    def draw(self, bird):
        self.draw_flying()
