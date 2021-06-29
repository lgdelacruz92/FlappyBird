import random

class PipeManager:
    def __init__(self, game):
        if game.config.num_pipes < 4:
            raise Exception('num_pipes in config should be at least 4')

        self.game = game
        self.paths = []
        for i in range(self.game.config.num_pipes):
            self.paths.append(self.get_path())

        # Get spacing
        screen_width = self.game.screen.get_width()
        spacing = self.game.config.pipe_spacing * screen_width
        self.scale = self.game.config.scale
        self.sprite_rect = (84, 323, 26, 160)

        # make rects
        self.paths_rects = []
        for i in range(self.game.config.num_pipes):
            self.paths_rects.append(
                (
                    screen_width + i * spacing,
                    self.paths[i][0],
                    self.sprite_rect[2] * self.scale,
                    self.paths[i][1] - self.paths[i][0]
                )
            )
    

    def update(self):
        '''
        Updates the pipes positions
        '''
        # Wrap the pipes around
        if self.paths_rects[1][0] < 0:
            temp = self.paths_rects[0]
            for i in range(1, len(self.paths_rects)):
                self.paths_rects[i-1] = self.paths_rects[i]
            temp = (self.game.screen.get_width(), temp[1], temp[2], temp[3])
            self.paths_rects[len(self.paths_rects) - 1] = temp

        # Update the pipe
        dt = self.game.clock.get_time()
        rate = self.game.config.floor_rate * dt
        for i in range(self.game.config.num_pipes):
            path_rect = self.paths_rects[i]
            new_rect = (path_rect[0] - rate, path_rect[1], path_rect[2], path_rect[3])
            self.paths_rects[i] = new_rect

    def get_path(self):
        bird_path = self.game.config.bird_path
        screen_height = self.game.screen.get_height()

        lower_limit = bird_path * screen_height
        upper_limit = screen_height - 2 * bird_path * screen_height

        # Map value
        value = random.randint(int(lower_limit), int(upper_limit))
        return (value, int(value + bird_path * screen_height))

    def get_pipes_rects(self):
        '''
        This methods returns the number of rects representing each pipes
        '''
        result = []
        for path_rect in self.paths_rects:
            # Top pipe
            x = path_rect[0]
            y = 0
            w = path_rect[2]
            h = path_rect[1]
            result.append((x, y, w, h))

            # Bottom pipe
            x = path_rect[0]
            y = path_rect[1] + path_rect[3]
            w = path_rect[2]
            h = self.game.screen.get_height() - (path_rect[1] + path_rect[3])
            result.append((x, y, w, h))
        return result