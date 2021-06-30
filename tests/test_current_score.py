import unittest
from unittest.mock import Mock

from src.static.current_score import CurrentScore


class TestCurrentScore(unittest.TestCase):
    def test_validate_string_score_1(self):
        '''
        Any alphabet is not valid
        '''
        game = Mock()
        current_score = CurrentScore(game)

        with self.assertRaises(ValueError):
            current_score.validate("abc")

        with self.assertRaises(ValueError):
            current_score.validate("-1")

        with self.assertRaises(ValueError):
            current_score.validate('1002')

        with self.assertRaises(ValueError):
            current_score.validate("12ab1")

        for i in range(1000):
            current_score.validate(f'{i}')
