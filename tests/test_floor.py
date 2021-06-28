import unittest
import json
from unittest.mock import Mock
from game import Game
from src.floor.floor import Floor


class TestFloor(unittest.TestCase):
    def test_get_rect(self):
        '''
        Test that get_rect returns proper values
        '''
        floor = Floor(0, 0, 200, 50, None)
        rect = floor.get_rect()
        expected_rect = (0, 0, 200, 50)
        self.assertEqual(rect, expected_rect)

    def test_set_rect(self):
        '''
        Test that set rect is working
        '''
        floor = Floor(0, 0, 200, 50, None)
        new_rect = (5, 5, 205, 55)
        expected_rect = (5, 5, 205, 55)
        floor.set_rect(new_rect)
        self.assertEqual(floor.get_rect(), expected_rect)