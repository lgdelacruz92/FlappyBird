import pygame
from utils.spritesheet import SpriteSheet


class FloorRenderer(pygame.sprite.Sprite):
    def __init__(self, floor_manager, game):
        # Game global
        self.game = game
        self.floor_manager = floor_manager
        sprite_width = self.game.config.sprite_floor_width
        sprite_height = self.game.config.sprite_floor_height
        self.sprite_rect = (292, 1, sprite_width, sprite_height)
        self.sprite_width = self.sprite_rect[2]
        self.floor_img = self.game.spritesheet.image_at(self.sprite_rect, colorkey=(255, 255, 255))


    def draw(self):
        for floor in self.floor_manager.floors:
            self.game.screen.blit(self.floor_img, floor.get_rect())
