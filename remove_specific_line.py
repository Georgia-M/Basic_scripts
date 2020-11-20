'''remove the lines from a file that start with a specific word'''

import os

thisdir = os.getcwd()

#change the path according to the folder
for r, d, f in os.walk('C:/Users/user/Desktop/test1'):
    for file in f:
        if file.endswith('.txt'):
            #change path every time, unless it won't work
            #open() function needs the full path always
            with open('C:/Users/user/Desktop/test1/'+file, "r+") as file1:
                lines = file1.readlines()

                #go to the begining of the file
                file1.seek(0)
                #erase everything form the file
                file1.truncate()

            #rewrite all the lines that don't start with BAD
            with open('C:/Users/user/Desktop/test1/'+file, "w+") as file2:
                for line in lines:
                    if not line.startswith("BAD"):
                        file2.write(line)
            

            file2.close()
            file1.close()
            
#don't forget to close the files, it won't work properly 
