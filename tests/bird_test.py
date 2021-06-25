from src.player.bird import Bird
from utils.config import Config
import unittest
import json

initial_bird_x = 0
initial_bird_y = 0


class TestBird(unittest.TestCase):
    def _make_bird(self):
        bird = None
        config = None
        with open('config.json', 'r') as config_file:
            config = Config(json.loads(config_file.read()))
            bird = Bird(initial_bird_x, initial_bird_y)
        return (bird, config)

    def test_bird_initialization(self):
        '''
        Tests if missing any parameters
        '''
        with self.assertRaises(Exception):
            Bird()

        with self.assertRaises(Exception):
            Bird(2)

        self._make_bird()

    def test_bird_falling_on_update(self):
        '''
        Tests that bird falls on updates
        '''
        bird, config = self._make_bird()
        bird.add_force(config.gravity)
        bird.update()
        self.assertTrue(bird.v > 0)

    def test_bird_gravity_fall_rate(self):
        '''
        Tests that checks the fall rate is accurate
        '''
        # g = 1
        # v = 0
        # y = 0
        bird, config = self._make_bird()
        self.assertEqual(bird.y, initial_bird_y)

        bird.add_force(config.gravity)
        bird.update()
        # v = 1
        # y = 1
        self.assertEqual(bird.y, initial_bird_y + 1 * config.gravity)

        bird.add_force(config.gravity)
        bird.update()
        # v = 2
        # y = 3
        self.assertEqual(bird.y, initial_bird_y + 3 * config.gravity)

        bird.add_force(config.gravity)
        bird.update()
        # v = 3
        # y = 6
        self.assertEqual(bird.y, initial_bird_y + 6 * config.gravity)

        bird.add_force(config.gravity)
        bird.update()
        # v = 4
        # y = 10
        self.assertEqual(bird.y, initial_bird_y + 10 * config.gravity)

        bird.add_force(config.gravity)
        bird.update()
        # v = 5
        # y = 15
        self.assertEqual(bird.y, initial_bird_y + 15 * config.gravity)

    def test_bird_force_up(self):
        '''
        Tests that bird goes up on force
        '''
        bird, config = self._make_bird()
        bird.add_force(config.gravity)
        bird.add_force(config.force_up)
        bird.update()
        self.assertTrue(bird.v < 0)


if __name__ == '__main__':
    unittest.main()
