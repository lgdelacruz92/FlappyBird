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
        self.angle = 0

    def update(self):
        dt = self.game.clock.get_time()
        self.v += self.g
        if self.v < self.game.config.velocity_up_limit:
            self.v = self.game.config.velocity_up_limit
        self.y += self.v * dt
        self.g = 0
        if self.v < 0:
            self.angle = self.game.config.flying_angle
        if self.v > 0.7:
            self.angle = -self.game.config.flying_angle

    def add_force(self, force, gravity):
        self.g += force
        self.g += gravity
