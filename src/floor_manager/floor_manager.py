class FloorManager:
    def __init__(self, floors, game):
        self.game = game
        if len(floors) < 2:
            raise ValueError('The number floors must be at least 2')
        self.floors = floors
        for i, floor in enumerate(self.floors):
            orig_rect = floor.get_rect()
            new_floor_y = self.game.screen.get_height() - orig_rect[3]
            new_rect = (i * orig_rect[2], new_floor_y, orig_rect[2], orig_rect[3])
            floor.set_rect(new_rect)

    def update(self):
        '''
        Updates the floors movement
        '''
        for floor in self.floors:
            orig_rect = floor.get_rect()
            dt = self.game.clock.get_time()
            new_floor_x = orig_rect[0] - (self.game.config.floor_rate * dt)
            new_rect = (new_floor_x, orig_rect[1], orig_rect[2], orig_rect[3])
            floor.set_rect(new_rect)