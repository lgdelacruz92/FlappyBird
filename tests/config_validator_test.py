import unittest
from utils.config_validator import validate_config


class ConfigValidator(unittest.TestCase):
    def test_validate_config_1(self):
        '''
        Tests to make sure config has all configs defined
        '''

        config = {}
        with self.assertRaises(KeyError):
            validate_config(config)

        config['birdImgUrl'] = 'some_url'
        with self.assertRaises(KeyError):
            validate_config(config)
        
        config['gravity'] = 1
        validate_config(config)

if __name__ == '__main__':
    unittest.main()
