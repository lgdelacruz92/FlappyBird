class Config:
    def __init__(self, config_json):
        self.validate_config(config_json)

    def validate_config(self, config_json):
        self.falling_bird_url = config_json['falling_bird_url']
        self.flying_bird_url = config_json['flying_bird_url']
        self.gravity = config_json['gravity']
        self.force_up = config_json['force_up']
        self.vlimit = config_json['vlimit']
        self.scale = config_json['scale']
