import unittest
from utils.config import Config


class TestConfig(unittest.TestCase):
    def test_config_initialization(self):
        '''
        Tests to make sure config has all configs defined
        '''

        config_json = {}
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['falling_bird_url'] = 'some_url'
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['gravity'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['force_up'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['vlimit'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['scale'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['flying_bird_url'] = 'some_url'
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['flying_angle'] = 1

        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['frame_rate'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['floor_pos'] = 1
        Config(config_json)


if __name__ == '__main__':
    unittest.main()
