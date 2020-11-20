'''compare the values from two text files with the same name but with different extension'''

import os

#paths
folder_path = "..."
first_value_file_path = "..."
second_value_file_path = "..."

#for statistics
num = 0
warnings = 0

#take the values from first folder
for r, d, f in os.walk(first_value_file_path):
    for first_file in f:
        if first_file.endswith(".txt"):
            #take the name of the file (without extension)
            base = os.path.basename(first_file)
            file1 = os.path.splitext(base)[0]

            #take the values from second folder
            for r, d, f in os.walk(second_value_file_path):
                for second_file in f:
                    if second_file.endswith(".dat"):
                        #take the name of the file without extension
                        base = os.path.basename(dipole_vmd)
                        file2 = os.path.splitext(base)[0]
                        
                        #if the two names of the files are the same
                        if file2 == file1:
                            
                            num += 1

                            #take the values from each one (first and second)
                            file_1 = open(first_value_file_path+first_file)
                            for line in file_1:
                                value_first_file = float(line)
                            file_2 = open(second_value_file_path+second_file)
                            for line in file_2:
                                value_second = float(line)

                            #find their deviation
                            if value_first < value_second:
                                per_cent = ((value_second - value_first)/value_second)*100
                            if value_code > value_vmd:
                                per_cent = ((value_first - value_second)/value_first)*100
                            if value_first == value_second:
                                per_cent = 0

                            #turn the deviation value into a string
                            string_percent = str(per_cent)

                            #create a file that says what the deviation is
                            new_file = open(folder_path+'/'+file1+'.txt', 'w+')
                            new_file.write('The devation of the two values is '+string_percent+' %')

                            #check if the deviation is too big
                            if per_cent > 1:
                                new_file.write('\nWARNING: DEVATION GREATER THAN 1%, VALUES MAY NOT MATCH')
                                warnings += 1

                            new_file.close()

#create the 'statistics' folder
string_num = str(num)
string_warnings = str(warnings)
new_file = open(folder_path+'/contrast_results.txt', 'w+')
new_file.write('The total of values that have been compared are: '+string_num+'\n')
new_file.write('The values which may not match (devation greater than 1%) are: '+string_warnings)
new_file.close()

