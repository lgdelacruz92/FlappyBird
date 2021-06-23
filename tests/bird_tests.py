import unittest

from game import Game
from src.player.bird import Bird


class BirdTest(unittest.TestCase):
    def test_bird_falling(self):
        g = Game(gravity=0.1)
        b = Bird(10, 10, game=g)

        # on x amount of updates bird should have a positive velocity
        b.update()
        b.update()

        self.assertTrue(b.velocity > 0)


if __name__ == '__main__':
    unittest.main()
