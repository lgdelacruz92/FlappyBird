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

        floors = [Floor(0, 0, 200, 50, game), Floor(0, 0, 200, 50, game)]

        floor_manager = FloorManager(floors, game)
        self.assertEqual(floor_manager.floors[0].y, 350)

    def test_manager_update_floors(self):
        '''
        Manager should be up be updating floors
        '''

        SCREEN_HEIGHT = 400
        game = Mock()
        game.screen.get_height.return_value = SCREEN_HEIGHT

        # set floor rate
        floor_rate = 2
        game.config.floor_rate = floor_rate

        # set delta time
        dt = 2
        game.clock.get_time.return_value = dt

        FLOOR_WIDTH = 200
        floors = [Floor(0, 0, FLOOR_WIDTH, 50, game)]
        with self.assertRaises(ValueError) as value_error:
            FloorManager(floors, game)

        floors.append(Floor(0, 0, FLOOR_WIDTH, 50, game))
        floors.append(Floor(0, 0, FLOOR_WIDTH, 50, game))

        # Floor manager
        floor_manager = FloorManager(floors, game)
        floor_manager.update()

        self.assertEqual(floor_manager.floors[0].x, -floor_rate * dt)
        self.assertEqual(floor_manager.floors[1].x, -floor_rate * dt + FLOOR_WIDTH)
        self.assertEqual(floor_manager.floors[2].x, -floor_rate * dt + FLOOR_WIDTH * 2)

    def test_floor_wraps_around(self):
        '''
        Make sure the floors wraps around
        '''

        SCREEN_HEIGHT = 400
        game = Mock()
        game.screen.get_height.return_value = SCREEN_HEIGHT

        # set floor rate
        floor_rate = 2
        game.config.floor_rate = floor_rate

        # set delta time
        dt = 2
        game.clock.get_time.return_value = dt

        FLOOR_WIDTH = 200
        floors = []
        for _ in range(3):
            floors.append(Floor(-FLOOR_WIDTH, 0, FLOOR_WIDTH, 50, game))

        # floor manager
        floor_manager = FloorManager(floors, game)
        floor_manager.update()

        self.assertEqual(floor_manager.floors[0].x, -floor_rate * dt)
        self.assertEqual(floor_manager.floors[1].x, -floor_rate * dt + FLOOR_WIDTH)
        self.assertEqual(floor_manager.floors[2].x, -floor_rate * dt + FLOOR_WIDTH * 2)