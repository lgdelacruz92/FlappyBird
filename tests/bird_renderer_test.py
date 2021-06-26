from src.player.bird_renderer import BirdRenderer
from unittest.mock import Mock
from unittest import TestCase


class TestBirdRenderer(TestCase):
    def _make_bird_renderer(self):
       # Mock dependencies
        game = Mock()
        surface_mock = Mock()
        game.pygame.image.load.return_value = surface_mock
        surface_mock.get_height.return_value = 1
        surface_mock.get_width.return_value = 1
        game.scale = 1

        # Mock bird
        bird = Mock()

        return BirdRenderer(game) 

    def test_bird_renderer_draw_1(self):
        '''
        Bird should use falling draw when falling
        '''
        bird_renderer = self._make_bird_renderer()

        # Make bird
        bird = Mock()
        bird.v = 1

        # Call draw
        bird_renderer.draw_falling = Mock()
        bird_renderer.draw(bird)

        self.assertEqual(bird_renderer.draw_falling.call_count, 1)

    def test_bird_renderer_draw_2(self):
        '''
        Bird should use flying draw when flying
        '''
        bird_renderer = self._make_bird_renderer()

        # Make bird
        bird = Mock()
        bird.v = -1

        # Call draw
        bird_renderer.draw_flying = Mock()
        bird_renderer.draw(bird)

        self.assertEqual(bird_renderer.draw_flying.call_count, 1)
