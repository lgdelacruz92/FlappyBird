import pygame

from src.player.bird_renderer import BirdRenderer
from src.player.bird import Bird
from game import Game
import json
from utils.config import Config
from utils.colors import GameColors

config = None
# Get configuration
with open('config.json', 'r') as config_file:
    config_json = json.loads(config_file.read())
    config = Config(config_json)

# Initialize pygame
pygame.init()

# Initialize game colors
game_colors = GameColors()

# Globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
SCALE = 1

# Set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize the global game
GAME = Game(
    pygame=pygame,
    scale=SCALE,
    screen=screen,
    config=config,
    game_colors=game_colors
    )

# Set up bird
pygame.display.set_caption('Bird')
bird_renderer = BirdRenderer(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, GAME)
bird = Bird(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, config)

run = True
while run:
    screen.fill(game_colors.black)
    bird.update()
    bird_renderer.draw(bird)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

pygame.quit()
