class Floor:
    def __init__(self, x, y, w, h, game):
        self.game = game
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.y = self.game.screen.get_height() - h

    def update(self):
        dt = self.game.clock.get_time()
        floor_rate = self.game.config.floor_rate
        self.x -= dt * floor_rate

    def get_rect(self):
        return (self.x, self.y, self.w, self.h)