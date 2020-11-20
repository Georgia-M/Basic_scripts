'''check if two files in different directories have the same name'''

import os
import glob

first_files_path = '...'
second_files_path = '...'

for r, d, f in os.walk(first_files_path):
    for first_file in f:
        if first_file.endswith(".txt"):
            #keep only the name (without .txt)
            base_first = os.path.basename(first_files_path+'\\'+first_file)
            first_file_name = os.path.splitext(base_first)[0]

            files = glob.glob(second_files_path+'\\*.dat')
            for second_file in files:
                #keep only the name
                base_second = os.path.basename(second_file)
                second_file_name = os.path.splitext(base_second)[0]

                if second_file_name == first_file_name:
                    print("same name")
