class Bird:
    def __init__(self, x: int, y: int, config):
        '''
        Initialize bird object
        '''
        if x is None or y is None or config is None:
            raise Exception('x and y, and config, parameters are required')
        self.x = x
        self.y = y
        self.v = 0
        self.g = 0
        self.config = config

    def update(self):
        self.v += self.g
        self.y += self.v
        self.g = 0

    def add_force(self, force, gravity):
        if self.v > self.config.vlimit:
            self.g += force
        self.g += gravity
