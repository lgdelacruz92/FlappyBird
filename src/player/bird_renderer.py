import pygame


class BirdRenderer(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
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
        self.image = pygame.transform.scale(
            img, (int(img.get_width() * scale), int(img.get_height() * scale)))

        # add rect
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        self.screen.blit(self.image, self.rect)
