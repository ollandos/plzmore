import os
import glob


conf_files_path = os.path.join(os.path.dirname(__file__), '*.conf.py')
conffiles = glob.glob(conf_files_path)
conffiles.sort()

for f in conffiles:
    exec(open(os.path.abspath(f)).read())
