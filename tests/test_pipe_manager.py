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
        game.config.bird_path = BIRD_PATH

        pipe_manager = PipeManager(game)

        for i in range(1000):
            pipe_path = pipe_manager.get_path()
            self.assertTrue(pipe_path[0] >= BIRD_PATH * SCREEN_HEIGHT)
            self.assertTrue(pipe_path[1] <= SCREEN_HEIGHT - BIRD_PATH * SCREEN_HEIGHT)
