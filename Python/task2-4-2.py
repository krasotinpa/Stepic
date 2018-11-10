import os

for cur_dir, dir, files in os.walk("main"):
    if any([f[-3:] == '.py' for f in files]):
        print(cur_dir)