class FloorManager:
    def __init__(self, floors, game):
        self.game = game
        self.floors = floors
        for floor in self.floors:
            orig_rect = floor.get_rect()
            new_floor_y = self.game.screen.get_height() - orig_rect[3]
            new_rect = (orig_rect[0], new_floor_y, orig_rect[2], orig_rect[3])
            floor.set_rect(new_rect)
