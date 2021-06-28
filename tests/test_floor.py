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

    def test_floor_update(self):
        '''
        Test that floor moves to the left according to game floor rate
        '''
        # initalize screen
        SCREEN_WIDTH = 400
        SCREEN_HEIGHT = 400
        screen = Mock()
        screen.get_width.return_value = SCREEN_WIDTH
        screen.get_height.return_value = SCREEN_HEIGHT

        # config
        floor_rate_num = 5
        config = Mock()
        config.floor_rate = floor_rate_num

        # pygame
        dt = 2
        clock = Mock()
        clock.get_time.return_value = dt

        # initialize game
        self.game = Game(screen=screen, config=config, clock=clock)

        floor = Floor(0, 0, 200, 50, self.game)
        floor.update()
        self.assertEqual(floor.x, -floor_rate_num * dt)
        floor.update()
        self.assertEqual(floor.x, -floor_rate_num * 2 * dt)

    def test_get_rect(self):
        '''
        Test that get_rect returns proper values
        '''
        #initialize screen
        SCREEN_HEIGHT = 400
        screen = Mock()
        screen.get_height.return_value = SCREEN_HEIGHT

        # initialize game
        self.game = Game(screen=screen)

        floor = Floor(0, 0, 200, 50, self.game)
        rect = floor.get_rect()
        expected_rect = (0, 350, 200, 50)
        self.assertEqual(rect, expected_rect)