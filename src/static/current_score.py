class CurrentScore:
    def __init__(self, game):
        self.game = game

    def get_rects(self, num_rects, x_offset, y_offset):
        if num_rects < 1 or num_rects > 3:
            raise ValueError(f'number of rects must only be between 1 - 3 (inclusive)')
        big_nums_scale = self.game.config.big_nums_scale
        screen_width = self.game.screen.get_width()
        screen_height = self.game.screen.get_height()
        height = int(big_nums_scale * screen_height)
        big_nums_width = self.game.config.big_nums["zero"][2]
        big_nums_height = self.game.config.big_nums["zero"][3]

        rects = []
        for i in range(num_rects):
            width = int(big_nums_width * (height / big_nums_height))
            x = screen_width // 2 + (i * (width))
            x -= (width // 2 - x_offset) 

            y = screen_height // 2
            y -= height // 2 - y_offset
            rects.append((x, y, width, height))
        return rects

    def validate(self, str_num):
        '''
        Valid score is only between 1 to 3 digits (inclusive)
        and only digits e.g (0-999)
        '''
        num = int(str_num)
        str_num_2 = str(num)
        if str_num != str_num_2 or num < 0 or num > 999:
            raise ValueError(f'{str_num} is not a valid score. It should only be between 0 - 999 (inclusive)')
        return num