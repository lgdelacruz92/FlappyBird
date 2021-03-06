import pygame
from src.player.bird_renderer import BirdRenderer
from src.player.bird import Bird
from game import Game
from game_manager import GameManager, IDLE, PLAYING, GAME_OVER
import json
from utils.config import Config
from utils.colors import GameColors
from utils.spritesheet import SpriteSheet
from utils.make_floors import make_floors

from src.background.background_renderer import BackgroundRenderer

from src.pipe.pipe import Pipe
from src.pipe.pipe_renderer import PipeRenderer
from src.pipe_manager.pipe_manager import PipeManager

from src.floor.floor import Floor
from src.floor_manager.floor_manager import FloorManager
from src.floor.floor_renderer import FloorRenderer

from src.static.score_board_renderer import ScoreBoardRenderer

from src.static.current_score import CurrentScore
from src.number.number_render_manager import NumberRenderManager

from src.static.score_ticker import ScoreTicker
from src.medal.medal_renderer import MedalRenderer

from src.static.db import BestScoreDB

from utils.collide import collide

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
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5625)

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
bird = Bird(SCREEN_WIDTH * 0.20, SCREEN_HEIGHT/2, GAME)

# Set up floor
floors = make_floors(GAME)
floor_manager = FloorManager(floors, GAME)
floor_renderer = FloorRenderer(floor_manager, GAME)

# Setup pipes
pipe = Pipe(SCREEN_WIDTH - 100, SCREEN_HEIGHT/3, 26, 160, GAME)
pipe_renderer = PipeRenderer(GAME)
pipe_manager = PipeManager(GAME)

# Score board renderer
score_board_renderer = ScoreBoardRenderer(GAME)

# current_score
current_score = CurrentScore(GAME)
number_render_manager = NumberRenderManager(GAME)
score_ticker = ScoreTicker()

# best score
best_score_ui = CurrentScore(GAME)
best_score_manager = NumberRenderManager(GAME)

# medal renderer
medal_renderer = MedalRenderer(score_board_renderer, GAME)

best_score_db = BestScoreDB()

run = True

while run:
    GAME.clock.tick(GAME.config.frame_rate)

    if bird.y < -200:
        GAME.game_manager.set_status(GAME_OVER)

    if bird.y >= floor_manager.get_floor_y() - 50:
        bird.y = floor_manager.get_floor_y() - 50
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
                elif GAME.game_manager.status == GAME_OVER:
                    bird.reset()
                    pipe_manager.reset()
                    GAME.game_manager.set_status(PLAYING)
                    score_ticker.reset()

    # screen fill
    screen.fill((84, 192, 201))

    # Background render
    background_render.draw()

    # Draw bird
    bird_renderer.draw(bird)

    if GAME.game_manager.status == PLAYING or GAME.game_manager.status == IDLE:
        floor_manager.update()
        pipe_manager.update()

    # Draw pipe
    pipes_rects = pipe_manager.get_pipes_rects()
    for i, pipe_rect in enumerate(pipes_rects):
        if i % 2 == 1:
            pipe_renderer.draw(pipe_rect, flip=False)
        else:
            pipe_renderer.draw(pipe_rect, flip=True)

    bird_rect = bird_renderer.bird_imgs[0].get_rect()
    offset_x = 0.25 * bird_rect[2]
    offset_y = 0.25 * bird_rect[3]

    bird_rect = (bird.x + offset_x, bird.y + offset_y, bird_rect[2] - offset_x * 2, bird_rect[2] - offset_y * 2)
    for pipe_rect in pipes_rects:
        if collide(bird_rect, pipe_rect):
            GAME.game_manager.set_status(GAME_OVER)

    if GAME.game_manager.status == GAME_OVER:
        score_board_renderer.draw()

        # current score
        score = score_ticker.get_score_str()
        score_num = current_score.validate(score)
        score_rects = current_score.get_rects(len(score), GAME.config.current_score_x_offset, GAME.config.current_score_y_offset)
        number_render_manager.big_nums_draw(score, score_rects)

        if score_num > best_score_db.get_best_score():
            # update best score in db
            best_score_db.update_best_score(score_num)

        # medal
        medal_renderer.draw_medal(score_num)

        # best score
        best_score_num = best_score_db.get_best_score() # Get it from db
        string_best_score = str(best_score_num)
        best_score_ui.validate(string_best_score)
        best_score_rects = best_score_ui.get_rects(len(string_best_score), GAME.config.best_score_x_offset, GAME.config.best_score_y_offset)
        best_score_manager.big_nums_draw(string_best_score, best_score_rects)

    score_ticker.update(bird, pipes_rects)

    # Draw floor
    floor_renderer.draw()


    pygame.display.update()

pygame.quit()
