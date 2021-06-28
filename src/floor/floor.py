class Floor:
    def __init__(self, x, y, w, h, game):
        self.game = game
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_rect(self):
        return (self.x, self.y, self.w, self.h)

    def set_rect(self, rect):
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]