

import os

with open('failed_paths.txt') as f:
    failed = f.read().splitlines()
    
[os.unlink(file_path) for file_path in failed]