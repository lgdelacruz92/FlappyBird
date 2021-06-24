from src.player.bird import Bird
from utils.config import Config
import unittest
import json


class TestBird(unittest.TestCase):
    def _make_bird(self):
        bird = None
        with open('config.json', 'r') as config_file:
            config = Config(json.loads(config_file.read()))
            bird = Bird(2, 3, config)
        return bird

    def test_bird_initialization(self):
        '''
        Tests if missing any parameters
        '''
        with self.assertRaises(Exception):
            Bird()

        with self.assertRaises(Exception):
            Bird(2)

        with self.assertRaises(Exception):
            Bird(2, 3)

        self._make_bird()

    def test_bird_falling_on_update(self):
        '''
        Tests that bird falls on updates
        '''
        bird = self._make_bird()
        bird.update()
        self.assertTrue(bird.v > 0)
    
    def test_bird_force_up(self):
        '''
        Tests that bird goes up on force
        '''
        bird = self._make_bird()
        bird.add_force(-5)
        bird.update()
        self.assertTrue(bird.v < 0)


if __name__ == '__main__':
    unittest.main()
