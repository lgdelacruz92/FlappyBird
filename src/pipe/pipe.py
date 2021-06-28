class Pipe:
    def __init__(self, x, y, w, h, game):
        self.game
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = self.game.config.pipe_velocity

    def update(self):
        self.x -= self.v

    def get_rect(self):
        return (self.x, self.y, self.w, self.h)
