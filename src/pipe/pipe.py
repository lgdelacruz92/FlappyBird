class Pipe:
    def __init__(self, x, y, w, h, game):
        self.game = game
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = self.game.config.floor_rate

    def update(self):
        dt = self.game.clock.get_time()
        self.x -= self.v * dt
        if self.x < -self.w * self.game.config.scale:
            self.x = self.game.screen.get_width() + 5

    def get_rect(self):
        return (self.x, self.y, self.w * self.game.config.scale, self.h * self.game.config.scale)
