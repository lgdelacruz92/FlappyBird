class Game:
    def __init__(self,
                 pygame=None,
                 scale=1,
                 screen=None,
                 gravity=0.1,
                 config=None,
                 game_colors=None
                 ):
        self.pygame = pygame
        self.scale = scale
        self.screen = screen
        self.config = config
        self.game_colors = game_colors

