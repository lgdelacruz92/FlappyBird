class Game:
    def __init__(self,
                 pygame=None,
                 screen=None,
                 gravity=0.1,
                 config=None,
                 game_colors=None,
                 game_manager=None,
                 spritesheet=None
                 ):
        self.pygame = pygame
        self.screen = screen
        self.config = config
        self.game_colors = game_colors
        self.game_manager = game_manager
        self.spritesheet = spritesheet
