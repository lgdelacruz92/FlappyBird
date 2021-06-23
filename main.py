import pygame
from src.player.bird import Bird

pygame.init()

# Globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
SCALE = 1

# Set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize the global game
GAME = {
    'pygame': pygame,
    'scale': SCALE,
    'screen': screen
}


pygame.display.set_caption('Bird')
player = Bird(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, GAME)


run = True
while run:

    player.draw()

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

pygame.quit()
