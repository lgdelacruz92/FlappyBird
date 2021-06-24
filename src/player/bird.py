class Bird:
    def __init__(self, x: int, y: int, config):
        '''
        Initialize bird object
        '''
        if not x or not y or config is None:
            raise Exception('x and y, and config, parameters are required')
        self.x = x
        self.y = y
        self.v = 0
        self.f = 0
        self.g = config.gravity

    def update(self):
        self.g += self.f
        self.v += self.g
        self.y += self.v

    def add_force(self, force):
        self.f = force
