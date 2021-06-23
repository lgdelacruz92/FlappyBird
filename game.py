class Game:
    def __init__(self,
                 pygame=None,
                 scale=1,
                 screen=None,
                 gravity=0.1
                 ):
        self.pygame = pygame
        self.scale = scale
        self.screen = screen
