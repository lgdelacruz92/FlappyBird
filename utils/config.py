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
