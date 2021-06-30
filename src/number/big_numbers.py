class BigNumbers:
    def __init__(self, game):
        self.game = game
        self.imgs = []

        big_nums_scale = self.game.config.big_nums_scale
        screen_height = self.game.screen.get_height()
        height = int(big_nums_scale * screen_height)
        big_nums_height = self.game.config.big_nums["zero"][3]

        scale = height/big_nums_height

        for i in range(10):
            img = self.game.spritesheet.image_at(self.get_num(i), colorkey=(255, 255, 255))
            img = self.game.pygame.transform.scale(img,
                (
                    int(img.get_width() * scale),
                    int(img.get_height() * scale)
                )
            )
            self.imgs.append(img)

    def get_imgs(self):
        return self.imgs

    def get_num(self, int_num):
        if int_num == 0:
            return self.game.config.big_nums['zero']
        elif int_num == 1:
            return self.game.config.big_nums['one']
        elif int_num == 2:
            return self.game.config.big_nums['two']
        elif int_num == 3:
            return self.game.config.big_nums['three']
        elif int_num == 4:
            return self.game.config.big_nums['four']
        elif int_num == 5:
            return self.game.config.big_nums['five']
        elif int_num == 6:
            return self.game.config.big_nums['six']
        elif int_num == 7:
            return self.game.config.big_nums['seven']
        elif int_num == 8:
            return self.game.config.big_nums['eight']
        elif int_num == 9:
            return self.game.config.big_nums['nine']
        else:
            raise ValueError(f'{int_num} is not a valid single digit number.')