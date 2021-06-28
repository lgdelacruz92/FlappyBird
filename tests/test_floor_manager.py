from unittest.mock import Mock
from src.floor_manager.floor_manager import FloorManager
import unittest
from src.floor.floor import Floor


class TestFloorManager(unittest.TestCase):
    def test_manager_positions_floors_in_right_y(self):
        '''
        Test that manager positions floors in the right y
        '''
        # initialize game
        SCREEN_HEIGHT = 400
        game = Mock()
        game.screen.get_height.return_value = SCREEN_HEIGHT

        floors = [Floor(0, 0, 200, 50, game)]

        floor_manager = FloorManager(floors, game)
        self.assertEqual(floor_manager.floors[0].y, 350)
