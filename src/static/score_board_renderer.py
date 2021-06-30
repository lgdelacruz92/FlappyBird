class ScoreBoardRenderer:
    def __init__(self, game):
        self.game = game
        self.sprite_rect = self.game.config.score_board_sprite_rect
        self.score_board_img = self.game.spritesheet.image_at(self.sprite_rect, colorkey=(255, 255, 255))
        self.scaler = self.game.config.score_board_height_percentage
        height = self.game.screen.get_height() * self.scaler
        score_board_original_width = self.sprite_rect[2]
        width = (self.game.screen.get_height() / height) * score_board_original_width
        self.score_board_img = self.game.pygame.transform.scale(self.score_board_img,
            (int(width), int(height)))

    def draw(self):
        current_rect = self.score_board_img.get_rect()

        # center x
        x = self.game.screen.get_width() // 2
        x -= current_rect[2] // 2

        # center y
        y = self.game.screen.get_height() // 2
        y -= current_rect[3] // 2

        new_rect = (x, y, current_rect[2], current_rect[3])
        self.game.screen.blit(self.score_board_img, new_rect)

