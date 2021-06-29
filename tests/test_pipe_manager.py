import unittest
from unittest.mock import Mock
from src.pipe_manager.pipe_manager import PipeManager


class TestPipeManager(unittest.TestCase):
    def test_get_path(self):
        '''
        Test that pipe manager gives proper path
        '''
        SCREEN_HEIGHT = 400
        BIRD_PATH = 0.10 # 10% of the screen height
        game = Mock()

        game.screen.get_height.return_value = SCREEN_HEIGHT
        game.config.pipe_sprite_rect = [0, 0, 26, 160]
        game.config.bird_path = BIRD_PATH
        game.config.num_pipes = 5
        game.config.scale = 1
        game.screen.get_width.return_value = 1
        game.config.pipe_spacing = 1

        pipe_manager = PipeManager(game)

        for i in range(1000):
            pipe_path = pipe_manager.get_path()
            self.assertTrue(pipe_path[0] >= BIRD_PATH * SCREEN_HEIGHT)
            self.assertTrue(pipe_path[1] <= SCREEN_HEIGHT - BIRD_PATH * SCREEN_HEIGHT)

    def test_get_pipes_rects(self):
        '''
        Test that it is giving the right pipes rects
        '''
        SCREEN_HEIGHT = 400
        SCREEN_WIDTH = 400
        BIRD_PATH = 0.10 # 10% of the screen height
        game = Mock()

        game.screen.get_height.return_value = SCREEN_HEIGHT
        game.config.bird_path = BIRD_PATH
        game.config.pipe_sprite_rect = [0, 0, 26, 160]
        game.config.num_pipes = 5

        game.screen.get_width.return_value = SCREEN_WIDTH
        game.config.pipe_spacing = 1

        pipe_manager = PipeManager(game)

        pipes_rects = pipe_manager.get_pipes_rects()
        self.assertEqual(len(pipes_rects), game.config.num_pipes * 2)

        sprite_rect = pipe_manager.sprite_rect
        self.assertEqual(pipes_rects[0][0], SCREEN_WIDTH)
        self.assertEqual(pipes_rects[0][1], -(SCREEN_HEIGHT - pipe_manager.paths_rects[0][1]))
        self.assertEqual(pipes_rects[0][2], 65.0)