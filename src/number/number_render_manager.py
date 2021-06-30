from src.number.big_numbers import BigNumbers
from src.number.small_numbers import SmallNumbers


class NumberRenderManager:
    def __init__(self, game):
        self.game = game
        self.small_nums = SmallNumbers(game)
        self.big_nums = BigNumbers(game)

    def big_nums_draw(self, str_num, rects):
        num_imgs = self.big_nums.get_imgs(str_num)
        for i, rect in enumerate(rects):
            self.game.screen.blit(num_imgs[i], rect)

    def small_nums_draw(self, str_num, rects):
        num_imgs = self.small_nums.get_imgs(str_num)
        for i, rect in enumerate(rects):
            self.game.screen.blit(num_imgs[i], rect)