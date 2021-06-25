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

        config_json['birdImgUrl'] = 'some_url'
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
        Config(config_json)


if __name__ == '__main__':
    unittest.main()
