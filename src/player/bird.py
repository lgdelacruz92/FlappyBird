class Bird:
    def __init__(self, x: int, y: int):
        '''
        Initialize bird object
        '''
        if x is None or y is None:
            raise Exception('x and y, and config, parameters are required')
        self.x = x
        self.y = y
        self.v = 0
        self.g = 0

    def update(self):
        self.v += self.g
        self.y += self.v
        self.g = 0

    def add_force(self, force):
        self.g += force
