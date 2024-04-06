from pathlib import Path
import os
import time
import shutil

path = Path('example-directory')
path.mkdir(exist_ok=True)

if not os.path.exists('test.txt'):
    with open('test.txt', 'w') as fp:
        fp.write('Hello, world!')

time.sleep(5)

shutil.move('test.txt', 'example-directory/')