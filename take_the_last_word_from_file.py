'''take a value from a file that has other things written in it too'''

import os

file_path = "..."

#for every .dat file keep the existent file and make a new one in .txt extension that only contains the dipole value
for r, d, f in os.walk(file_path):
    for file in f:
        if file.endswith(".dat"):
           
            dat_file = open(file_path+file)

            lines = []
            for line in dat_file:
                elem = line.split(' ')
                lines += elem

            new_file = open(file_path+file+'.txt', 'w+')

            #we assume the value is the last thing written
            new_file.write(lines[-1])
            new_file.close()

#or


#for every .dat file erase everything else and keep only the dipole value (edit the existent file without making a new one)
for r, d, f in os.walk(file_path):
    for file in f:
        if file.endswith(".dat"):
           
            dat_file = open(file_path+file, 'r+')

            lines = []
            for line in dat_file:
                elem = line.split(' ')
                lines += elem

            dat_file.seek(0)
            dat_file.truncate()

            #we assume the value is the last thing written
            new_file = open(file_path+file, 'w+')
            new_file.write(lines[-1])

            new_file.close()
            dat_file.close()

                                             
