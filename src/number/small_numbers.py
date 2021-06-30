class SmallNumbers:
    def __init__(self, game):
        self.game = game

    def get_num(self, int_num):
        if int_num == 0:
            return self.game.config.small_nums['zero']
        elif int_num == 1:
            return self.game.config.small_nums['one']
        elif int_num == 2:
            return self.game.config.small_nums['two']
        elif int_num == 3:
            return self.game.config.small_nums['three']
        elif int_num == 4:
            return self.game.config.small_nums['four']
        elif int_num == 5:
            return self.game.config.small_nums['five']
        elif int_num == 6:
            return self.game.config.small_nums['six']
        elif int_num == 7:
            return self.game.config.small_nums['seven']
        elif int_num == 8:
            return self.game.config.small_nums['eight']
        elif int_num == 9:
            return self.game.config.small_nums['nine']
        else:
            raise ValueError(f'{int_num} is not a valid single digit number.')