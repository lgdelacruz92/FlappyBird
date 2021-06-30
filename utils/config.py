class Config:
    def __init__(self, config_json):
        self.validate_config(config_json)

    def validate_config(self, config_json):
        self.gravity = config_json['gravity']
        self.force_up = config_json['force_up']
        self.vlimit = config_json['vlimit']
        self.scale = config_json['scale']
        self.flying_angle = config_json['flying_angle']
        self.frame_rate = config_json['frame_rate']
        self.floor_pos = config_json['floor_pos']
        self.background_pos = config_json['background_pos']
        self.floor_rate = config_json['floor_rate']
        self.pipe_velocity = config_json['pipe_velocity']
        self.sprite_floor_width = config_json['sprite_floor_width']
        self.sprite_floor_height = config_json['sprite_floor_height']
        self.sprite_background_width = config_json['sprite_background_width']
        self.sprite_background_height = config_json['sprite_background_height']
        self.velocity_up_limit = config_json['velocity_up_limit']
        self.bird_path = config_json['bird_path']
        self.num_pipes = config_json['num_pipes']
        self.pipe_spacing = config_json['pipe_spacing']
        self.pipe_sprite_rect = config_json['pipe_sprite_rect']
        self.score_board_sprite_rect = config_json['score_board_sprite_rect']
        self.score_board_height_percentage = config_json['score_board_height_percentage']
        self.small_nums = config_json['small_nums']
        self.big_nums = config_json['big_nums']
