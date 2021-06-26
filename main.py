import pygame
from src.player.bird_renderer import BirdRenderer
from src.player.bird import Bird
from game import Game
from game_manager import GameManager, IDLE, PLAYING, GAME_OVER
import json
from utils.config import Config
from utils.colors import GameColors
from utils.spritesheet import SpriteSheet
from src.static.floor_renderer import FloorRenderer
from src.static.background_renderer import BackgroundRenderer

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

# Set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initializse game manager
game_manager = GameManager()

# Initialize Spritesheet
spritesheet = SpriteSheet('img/spritesheet.png')

# Initialize clock
clock = pygame.time.Clock()

# Initialize the global game
GAME = Game(
    pygame=pygame,
    screen=screen,
    config=config,
    game_colors=game_colors,
    game_manager=game_manager,
    spritesheet=spritesheet,
    clock=clock
    )

# Setup background
background_render = BackgroundRenderer(GAME)

# Set up bird
pygame.display.set_caption('Bird')
bird_renderer = BirdRenderer(GAME)
bird = Bird(SCREEN_WIDTH * 0.20, SCREEN_HEIGHT/2, config)

# Set up floor
floor_renderer = FloorRenderer(GAME)

run = True

while run:
    GAME.clock.tick(GAME.config.frame_rate)

    if bird.y >= GAME.config.floor_pos - 50:
        bird.y = GAME.config.floor_pos - 50
        GAME.game_manager.set_status(GAME_OVER)

    if GAME.game_manager.status == PLAYING:
        bird.add_force(0, config.gravity)
        bird.update()

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                bird.add_force(config.force_up, 0)

                # Bird should be floating if game hasn't started yet
                if GAME.game_manager.status == IDLE:
                    GAME.game_manager.set_status(PLAYING)
    screen.fill((84, 192, 201))

    # Background render
    background_render.draw()

    # Draw bird
    bird_renderer.draw(bird)

    # Draw floor
    floor_renderer.update()
    floor_renderer.draw()

    pygame.display.update()

pygame.quit()
