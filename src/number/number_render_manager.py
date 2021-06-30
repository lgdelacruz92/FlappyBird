from src.number.big_numbers import BigNumbers
from src.number.small_numbers import SmallNumbers


class NumberRenderManager:
    def __init__(self, game):
        self.game = game
        self.small_nums = SmallNumbers(game)
        self.big_nums = BigNumbers(game)

    def big_nums_draw(self, str_num, rects):
        num_imgs = self.big_nums.get_imgs()
        imgs = []
        for i in range(len(str_num)):
            digit = int(str_num[i])
            imgs.append(num_imgs[digit])
        for i, rect in enumerate(rects):
            self.game.screen.blit(imgs[i], rect)

    def small_nums_draw(self, str_num, rects):
        num_imgs = self.small_nums.get_imgs()
        imgs = []
        for i in range(len(str_num)):
            digit = int(str_num[i])
            imgs.append(num_imgs[digit])
        for i, rect in enumerate(rects):
            self.game.screen.blit(imgs[i], rect)