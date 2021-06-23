import os
import sys

this_dir = os.path.dirname(__file__)
rel_dir = os.path.join(this_dir, '..')
abs_path = os.path.abspath(rel_dir)
sys.path.append(abs_path)
print(abs_path)
for path in sys.path:
    print(path)