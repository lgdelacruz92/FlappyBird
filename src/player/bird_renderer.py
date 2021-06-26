import pygame


class BirdRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Global game object
        self.game = game

        # pygame
        self.pygame = game.pygame
        self.pygame.sprite.Sprite.__init__(self)

        # load the bird img
        falling_bird_img = game.config.falling_bird_url
        falling_img = self.pygame.image.load(falling_bird_img)

        flying_bird_img = game.config.flying_bird_url
        flying_img = self.pygame.image.load(flying_bird_img)

        # get global game scale
        scale = game.config.scale

        # get global game scren
        self.screen = game.screen

        # add image
        self.falling_image = self.pygame.transform.scale(
            falling_img, (int(falling_img.get_width() * scale), int(falling_img.get_height() * scale)))
        self.flying_image = self.pygame.transform.scale(
            flying_img, (int(flying_img.get_width() * scale), int(flying_img.get_height() * scale)))

        # add rect
        self.rect = self.falling_image.get_rect()


    def draw_falling(self):
        self.screen.blit(self.falling_image, self.rect)

    def draw_flying(self):
        print('hello')

    def draw(self, bird):
        if bird.v < 0:
            self.draw_falling()
        else:
            self.draw_flying()
