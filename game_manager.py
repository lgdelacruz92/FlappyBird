IDLE = 1
PLAYING = 2
GAME_OVER = 3


class GameManager:
    def __init__(self, config):
        self.status = IDLE

    def set_status(self, status):
        self.status = status
    
    def get_status(self):
        return self.status