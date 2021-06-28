from src.floor.floor import Floor


def make_floors(game):
    floor_nums = game.screen.get_width() // game.config.sprite_floor_width
    floors = []
    for _ in range(floor_nums+2):
        floors.append(Floor(0, 0, game.config.sprite_floor_width, game.config.sprite_floor_height, game))
    return floors