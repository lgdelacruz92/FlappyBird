class BackgroundRenderer:
    def __init__(self, game):

        # Game global
        self.game = game
        self.width = game.screen.get_width()
        self.height = game.screen.get_height()
        sprite_width = game.config.sprite_background_width
        sprite_height = game.config.sprite_background_height
        floor_height = game.config.sprite_floor_height
        screen_height = game.screen.get_height()
        target_height = screen_height - floor_height
        scaler = target_height / sprite_height

        self.sprite_rect = (0, 1, sprite_width, sprite_height)
        self.background_img = game.spritesheet.image_at(self.sprite_rect, colorkey=(255, 255, 255))
        self.background_img = game.pygame.transform.scale(
            self.background_img,
            (int(self.background_img.get_width() * scaler), int(self.background_img.get_height() * scaler))
        )
        self.background_nums = int(game.screen.get_width() / self.background_img.get_width()) + 1

    def draw(self):
        start_rect = self.background_img.get_rect()
        start_x = start_rect[0]
        for i in range(self.background_nums):
            background_rect = (start_x + i * start_rect[2], 0, start_rect[2], start_rect[3])
            self.game.screen.blit(self.background_img, background_rect)

