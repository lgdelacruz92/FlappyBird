import pygame


class BirdRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Global game object
        self.game = game

        # pygame
        pygame = game.pygame
        pygame.sprite.Sprite.__init__(self)

        # load the bird img
        falling_bird_img = game.config.falling_bird_url
        falling_img = pygame.image.load(falling_bird_img)

        flying_bird_img = game.config.flying_bird_url
        flying_img = pygame.image.load(flying_bird_img)

        # get global game scale
        scale = game.scale

        # get global game scren
        self.screen = game.screen

        # add image
        self.falling_image = pygame.transform.scale(
            falling_img, (int(falling_img.get_width() * scale), int(falling_img.get_height() * scale)))
        self.flying_image = pygame.transform.scale(
            flying_img, (int(flying_img.get_width() * scale), int(flying_img.get_height() * scale)))

        # add rect
        self.rect = self.falling_image.get_rect()

        # Frame skip for wings
        self.frame_skip = 100
        self.frame_skip_toggle = True
        self.frame_skip_counter = 0

    def draw_falling(self):
        self.screen.blit(self.falling_image, self.rect)

    def draw_flying(self):
        if self.frame_skip_counter == self.frame_skip:
            self.frame_skip_counter = 0
            self.frame_skip_toggle = not self.frame_skip_toggle

        if self.frame_skip_toggle == True:
            self.screen.blit(self.flying_image, self.rect)
        else:
            self.draw_falling()
        self.frame_skip_counter += 1

    def draw(self, bird):
        self.rect.center = (bird.x, bird.y)
        if bird.v < 0:
            self.draw_falling()
        else:
            self.draw_flying()
