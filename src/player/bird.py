class Bird:
    def __init__(self, x: int, y: int, game):
        '''
        Initialize bird object
        '''
        self.game = game
        if x is None or y is None or self.game.config is None:
            raise Exception('x and y, and config, parameters are required')
        self.x = x
        self.y = y
        self.v = 0
        self.g = 0
        self.config = self.game.config

    def update(self):
        dt = self.game.clock.tick(self.game.config.frame_rate)
        self.v += self.g
        self.y += self.v * dt
        self.g = 0

    def add_force(self, force, gravity):
        self.g += force
        self.g += gravity
