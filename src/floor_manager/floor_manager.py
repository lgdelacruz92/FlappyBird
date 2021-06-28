class FloorManager:
    def __init__(self, floors, game):
        self.game = game
        if len(floors) < 2:
            raise ValueError('The number floors must be at least 2')
        self.floors = floors
        first_x = floors[0].get_rect()[0]
        for i, floor in enumerate(self.floors):
            orig_rect = floor.get_rect()
            new_floor_y = self.game.screen.get_height() - orig_rect[3]
            new_rect = (i * orig_rect[2] + first_x, new_floor_y, orig_rect[2], orig_rect[3])
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

        # If first floor is no longer on screen
        if self.floors[1].x < 0:
            #wrap around
            temp = self.floors[0]
            for i in range(1, len(self.floors)):
                self.floors[i-1] = self.floors[i]
            self.floors[len(self.floors)-1] = temp
            orig_rect = temp.get_rect()
            new_rect = (orig_rect[0] + len(self.floors) * orig_rect[2], orig_rect[1], orig_rect[2], orig_rect[3])
            self.floors[len(self.floors)-1].set_rect(new_rect)

