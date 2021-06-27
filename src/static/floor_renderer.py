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
        self.floor_nums = (self.width//self.sprite_width) + 2
        if self.floor_nums <= 2:
            raise Exception('This should not happen.')

        self.floor_imgs = []
        self.floor_img = self.game.spritesheet.image_at(self.sprite_rect, colorkey=-1)
        for i in range(self.floor_nums):
            self.floor_imgs.append(self.floor_img)

        self.rects = []
        for i in range(self.floor_nums):
            height = self.sprite_rect[3]
            new_rect = (
                (i * self.sprite_width),
                self.game.config.floor_pos,
                self.sprite_width,
                height
            )
            self.rects.append(new_rect)

    def update(self):
        if 1 <= self.floor_nums and self.rects[1][0] < 0:
            # Reorganize rects
            temp = self.rects[0]
            for i in range(1, self.floor_nums):
                self.rects[i-1] = self.rects[i]

            # upate position
            new_rect = (self.rects[self.floor_nums-1][0] + temp[2], temp[1], temp[2], temp[3])
            self.rects[self.floor_nums-1] = new_rect

        for i in range(self.floor_nums):
            height = self.sprite_rect[3]
            old_rect = self.rects[i]
            new_rect = (old_rect[0]-1, old_rect[1], old_rect[2], old_rect[3])
            self.rects[i] = new_rect

    def draw(self):
        for i in range(self.floor_nums):
            self.game.screen.blit(self.floor_imgs[i], self.rects[i])
