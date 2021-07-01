import unittest
from utils.collide import collide


class TestCollision(unittest.TestCase):
    def test_collision_1(self):
        '''
        Collision between to rectangles
        '''
        rect1 = (100, 100, 100, 100)
        rect2 = (100, -1, 100, 100)
        self.assertFalse(collide(rect1, rect2))

        rect2 = (100, 50, 100, 100)
        self.assertTrue(collide(rect1, rect2))

        rect2 = (100, 100, 100, 100)
        self.assertTrue(collide(rect1, rect2))

        rect2 = (200, 100, 100, 100)
        self.assertTrue(collide(rect1, rect2))

        rect2 = (0, 100, 100, 100)
        self.assertTrue(collide(rect1, rect2))

        rect2 = (-1, -1, 100, 100)
        self.assertFalse(collide(rect1, rect2))

        rect2 = (201, 201, 100, 100)
        self.assertFalse(collide(rect1, rect2))