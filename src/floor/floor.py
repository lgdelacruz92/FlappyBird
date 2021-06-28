class Floor:
    def __init__(self, x, y, w, h, game):
        self.game = game
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.y = self.game.screen.get_height() - h
