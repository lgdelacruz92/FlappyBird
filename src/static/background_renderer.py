class BackgroundRenderer:
    def __init__(self, backgrounds, game):

        # Game global
        self.game = game
        self.width = game.screen.get_width()
        self.height = game.screen.get_height()
        sprite_width = game.config.sprite_background_width
        sprite_height = game.config.sprite_background_height
        self.sprite_rect = (0, 1, sprite_width, sprite_height)
        self.background_img = game.spritesheet.image_at(self.sprite_rect, colorkey=(255, 255, 255))
        self.backgrounds = backgrounds

    def draw(self):
        for background in self.backgrounds:
            self.game.screen.blit(self.background_img, background.get_rect())

