import unittest
from unittest.mock import Mock
from src.static.score_ticker import ScoreTicker


class TestScoreTicker(unittest.TestCase):
    def test_score_ticker_1(self):
        pipes_rects = [(400, 0, 5, 400)]
        score_ticker = ScoreTicker()
        bird = Mock()
        bird.x = 399
        score_ticker.update(bird, pipes_rects)
        bird.x += 1
        score_ticker.update(bird, pipes_rects)
        bird.x += 1
        score_ticker.update(bird, pipes_rects)
        self.assertEquals(score_ticker.get_score(), 0)
        bird.x += 1
        score_ticker.update(bird, pipes_rects)
        bird.x += 1
        score_ticker.update(bird, pipes_rects)
        bird.x += 1
        score_ticker.update(bird, pipes_rects)
        bird.x += 1
        score_ticker.update(bird, pipes_rects)
        bird.x += 1
        score_ticker.update(bird, pipes_rects)
        self.assertEquals(score_ticker.get_score(), 1)