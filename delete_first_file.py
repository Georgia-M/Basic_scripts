'''delete the first file that it was created'''

import os

p = 'C:/Users/user/Downloads/'

min_time = 100000000000000000000000000000000000000000000

for r, d, f in os.walk(p):
    for file in f:
        if file.endswith('.txt'):
            creation_time = os.path.getctime(p+file)

            if creation_time < min_time:
                min_time = creation_time
                first_file = file

os.remove(p+first_file)
