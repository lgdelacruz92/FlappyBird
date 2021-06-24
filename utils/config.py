import json


class Config:
    def __init__(self, config_json):
        self.validate_config(config_json)

    def validate_config(self, config_json):
        self.birdImgUrl = config_json['birdImgUrl']
        self.gravity = config_json['gravity']
