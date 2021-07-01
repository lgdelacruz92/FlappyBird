class MedalRenderer:
    def __init__(self, score_board_renderer, game):
        self.game = game

        # Get sprites
        self.bronze_sprite_rect = self.game.config.bronze_medal_rect
        self.silver_sprite_rect = self.game.config.silver_medal_rect
        self.gold_sprite_rect = self.game.config.gold_medal_rect

        # calculate scale
        board_height = score_board_renderer.score_board_img.get_rect()[3]
        score_board_sprite_height = score_board_renderer.sprite_rect[3]
        scale = board_height / score_board_sprite_height

        # Make images
        self.bronze_medal_img = self._make_img(self.bronze_sprite_rect, scale)
        self.silver_medal_img = self._make_img(self.silver_sprite_rect, scale)
        self.gold_medal_img = self._make_img(self.gold_sprite_rect, scale)

    def _make_img(self, rect, scale):
        img = self.game.spritesheet.image_at(rect, colorkey=(255, 255, 255))
        img = self.game.pygame.transform.scale(
            img,
            (
                int(img.get_width() * scale),
                int(img.get_height() * scale)
            )
        )
        return img

    def get_rect(self):
        start_x = self.game.screen.get_width() // 2 + self.game.config.medal_pos_x_offset
        start_y = self.game.screen.get_height() // 2 + self.game.config.medal_pos_y_offset
        w = self.bronze_medal_img.get_width()
        h = self.bronze_medal_img.get_height()
        return (start_x, start_y, w, h)

    def draw_medal(self, score):
        if score <= 10:
            self.game.screen.blit(self.bronze_medal_img, self.get_rect())
        elif score <= 20:
            self.game.screen.blit(self.silver_medal_img, self.get_rect())
        else:
            self.game.screen.blit(self.gold_medal_img, self.get_rect())