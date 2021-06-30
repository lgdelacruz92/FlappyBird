import unittest
from utils.config import Config


class TestConfig(unittest.TestCase):
    def test_config_initialization(self):
        '''
        Tests to make sure config has all configs defined
        '''

        config_json = {}


        config_json['current_score_y_offset'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['current_score_y_offset'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['current_score_x_offset'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['small_nums_scale'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['big_nums_scale'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['big_nums'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['small_nums'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['score_board_height_percentage'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['score_board_sprite_rect'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['pipe_sprite_rect'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['pipe_spacing'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['num_pipes'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['bird_path'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['velocity_up_limit'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['sprite_background_height'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['sprite_background_width'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['sprite_floor_height'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['sprite_floor_width'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)



        config_json['pipe_velocity'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)


        config_json['floor_rate'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)

        config_json['background_pos'] = 1
        with self.assertRaises(KeyError):
            Config(config_json)

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
