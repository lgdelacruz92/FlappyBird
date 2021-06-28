import unittest
import json
from unittest.mock import Mock
from game import Game
from src.floor.floor import Floor


class TestFloor(unittest.TestCase):
    def test_floor_position(self):
        '''
        Test that floor is drawn in the right position
        '''

        # initalize screen
        SCREEN_WIDTH = 400
        SCREEN_HEIGHT = 400
        screen = Mock()
        screen.get_width.return_value = SCREEN_WIDTH
        screen.get_height.return_value = SCREEN_HEIGHT

        # initialize game
        self.game = Game(screen=screen)

        floor_height = 50

        floor = Floor(0,0,200, floor_height, self.game)
        self.assertEqual(floor.y, SCREEN_HEIGHT - floor_height)

