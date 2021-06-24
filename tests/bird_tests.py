from src.player.bird import Bird
from utils.config_validator import validate_config
import unittest
import json


class BirdTest(unittest.TestCase):
    def test_bird_falling_1(self):
        '''
        Tests if missing any parameters
        '''
        with self.assertRaises(Exception):
            Bird()

        with self.assertRaises(Exception):
            Bird(2)

        with self.assertRaises(Exception):
            Bird(2, 3)

        Bird(2, 3, {})


if __name__ == '__main__':
    unittest.main()
