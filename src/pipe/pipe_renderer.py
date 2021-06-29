import pygame
from utils.spritesheet import SpriteSheet


class PipeRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Game global
        self.game = game
        self.width = game.screen.get_width()
        self.height = game.screen.get_height()
        self.sprite_rect = self.game.config.pipe_sprite_rect
        self.pipe_img = self.game.spritesheet.image_at(self.sprite_rect, colorkey=(255, 255, 255))

    def draw(self, pipe_rect, flip=False):
        pipe_image = self.pipe_img
        if flip == True:
            pipe_image = self.game.pygame.transform.flip(self.pipe_img, False, True)
        scale_factor = self.height / self.pipe_img.get_height()
        scaled_pipe_img = self.game.pygame.transform.scale(pipe_image,
            (
                int(pipe_image.get_width() * scale_factor),
                int(pipe_image.get_height() * scale_factor)
            )
        )
        self.game.screen.blit(scaled_pipe_img, pipe_rect)