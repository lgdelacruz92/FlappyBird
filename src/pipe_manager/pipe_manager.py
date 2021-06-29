import random

class PipeManager:
    def __init__(self, game):
        self.game = game

    def get_path(self):
        bird_path = self.game.config.bird_path
        screen_height = self.game.screen.get_height()

        lower_limit = bird_path * screen_height
        upper_limit = screen_height - 2 * bird_path * screen_height

        # Map value
        value = random.randint(int(lower_limit), int(upper_limit))
        return (value, int(value + bird_path * screen_height))
