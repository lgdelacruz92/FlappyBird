import pygame
from utils.spritesheet import SpriteSheet


class FloorRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Game global
        self.game = game
        self.width = game.screen.get_width()
        self.height = game.screen.get_height()
        self.sprite_rect = (292, 1, 168, 55)
        self.sprite_width = self.sprite_rect[2]

        # The amount of floor drawings needed
        self.floor_nums = (self.width//self.sprite_width) + 1 

        self.floor_imgs = []
        self.floor_img = self.game.spritesheet.image_at(self.sprite_rect, colorkey=-1)
        for i in range(self.floor_nums):
            self.floor_imgs.append(self.floor_img)

    def draw(self):
        for i in range(self.floor_nums):
            height = self.sprite_rect[3]
            new_rect = (
                i * self.sprite_width,
                self.game.config.floor_pos,
                self.sprite_width,
                height
            )
            self.game.screen.blit(self.floor_imgs[i], new_rect)
