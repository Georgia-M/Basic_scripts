'''move specific files from downloads to another folder'''

import os

old_path = 'C:/Users/user/Downloads/'
new_path = 'C:/Users/user/Desktop/test'

for r, d, f in os.walk(old_path):
    for file in f:
        if file.endswith(".txt"):
            #os.replace or os.rename 
            os.replace(old_path+file, new_path+'/'+file)
