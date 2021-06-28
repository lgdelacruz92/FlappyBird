import pygame
from utils.spritesheet import SpriteSheet


class PipeRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Game global
        self.game = game
        self.width = game.screen.get_width()
        self.height = game.screen.get_height()
        self.sprite_rect = (84, 323, 26, 160)
        self.pipe_img = self.game.spritesheet.image_at(self.sprite_rect, colorkey=(255, 255, 255))
        self.pipe_img = self.game.pygame.transform.scale(self.pipe_img,
            (self.pipe_img.get_width() * self.game.config.scale,
            self.pipe_img.get_height() * self.game.config.scale
            )
        )

    def draw(self, pipe):
        self.game.screen.blit(self.pipe_img, pipe.get_rect())