import os
import sys
from utils.colors import bcolors


if len(sys.argv) < 2:
    s = bcolors.FAIL
    s += 'Config name should be added'
    s += bcolors.ENDC
    raise Exception(s)

cwd = os.getcwd()
abs_path = os.path.abspath(os.path.join(cwd, 'utils', 'config.py'))

with open(abs_path, 'a') as config_file:
    config_file.write(f'        self.{sys.argv[1]} = config_json[\'{sys.argv[1]}\']\n')


abs_path = os.path.abspath(os.path.join(cwd, 'tests', 'test_config.py'))
temp_file_path = os.path.abspath(os.path.join(cwd, 'tests', 'temp.py'))

temp_file = open(temp_file_path, 'w')
with open(abs_path, 'r') as config_test_file:
    for line in config_test_file:
        temp_file.write(line)
        if 'config_json = ' in line:
            new_config_line = [
                '\n',
                f'        config_json[\'{sys.argv[1]}\'] = 1',
                '        with self.assertRaises(KeyError):',
                '            Config(config_json)'
            ]
            temp_file.write('\n'.join(new_config_line))
            temp_file.write('\n')
            temp_file.write('\n')

os.system(f'rm {abs_path}')
os.system(f'mv {temp_file_path} {abs_path}')
