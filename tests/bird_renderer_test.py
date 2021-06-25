from src.player.bird_renderer import BirdRenderer
from unittest.mock import Mock
from unittest import TestCase


class TestBirdRenderer(TestCase):
    def test_bird_renderer_draw(self):
        '''
        Test that bird renderer flutters when velocity is up
        '''
        # Mock dependencies
        game = Mock()
        surface_mock = Mock()
        game.pygame.image.load.return_value = surface_mock
        surface_mock.get_height.return_value = 1
        surface_mock.get_width.return_value = 1
        game.scale = 1

        # Mock bird
        bird = Mock()

        bird_renderer = BirdRenderer(game)
        bird_renderer.draw_falling = Mock()
        bird_renderer.draw(bird)

        self.assertEqual(bird_renderer.draw_falling.call_count, 1)
