import pygame


class BirdRenderer(pygame.sprite.Sprite):
    def __init__(self, game):
        # Global game object
        self.game = game

        # pygame
        pygame = game.pygame
        pygame.sprite.Sprite.__init__(self)

        # load the bird img
        birdImg = game.config.birdImgUrl
        img = pygame.image.load(birdImg)

        # get global game scale
        scale = game.scale

        # get global game scren
        self.screen = game.screen

        # add image
        self.falling_image = pygame.transform.scale(
            img, (int(img.get_width() * scale), int(img.get_height() * scale)))

        # add rect
        self.rect = self.falling_image.get_rect()
    
    def draw_falling(self):
        self.screen.blit(self.falling_image, self.rect)

    def draw(self, bird):
        self.rect.center = (bird.x, bird.y)
        self.draw_falling()
