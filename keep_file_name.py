'''keep only the name of the file'''

import os
p = 'C:/Users/user/Desktop/test/dipole_value_from_vmd'
#for every file in the 'p' path
for r, d, f in os.walk(p):
    for file in f:
        if file.endswith(".txt"):
            #take only the name of the file, not the whole path (e.g. file.txt)
            base = os.path.basename(dipole_vmd)
            print(base)
            #take only the name of the file without the extension (e.g. file)
            file_name = os.path.splitext(base)[0]
  
