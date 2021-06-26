class BackgroundRenderer:
    def __init__(self, game):

        # Game global
        self.game = game
        self.width = game.screen.get_width()
        self.height = game.screen.get_height()
        self.sprite_rect = (0, 1, 142, 255)
        self.sprite_width = self.sprite_rect[2]

        # The amount of floor drawings needed
        self.background_nums = (self.width//self.sprite_width) + 1 

        self.background_imgs = []
        self.background_img = self.game.spritesheet.image_at(self.sprite_rect, colorkey=-1)
        for i in range(self.background_nums):
            self.background_imgs.append(self.background_img)
        self.y = 0

    def draw(self):
        for i in range(self.background_nums):
            height = self.sprite_rect[3]
            new_rect = (
                i * self.sprite_width,
                self.y,
                self.sprite_width,
                height
            )
            self.game.screen.blit(self.background_imgs[i], new_rect)
