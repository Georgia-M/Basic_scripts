'''rename all files in a folder according to files in another'''

import os

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

                #check if the name has already been named, if it has continue with the next one
                if second_file_name.startswith('complex'):
                    continue

                #get the new name
                second_new_file_name = first_file_name+'.dat'

                #if the same name already exists, continue with the next one
                new_name_path = second_files_path+'\\'+second_new_file_name
                if os.path.exists(new_name_path):
                    continue

                #rename the file
                else:
                    os.rename(second_file, new_name_path)

#the "for r, d, f in os.walk()" loop takes all the files in the path,
#in the "for file in f" the "file" is only the name of the file with its extension
#the "files = glob.glob(path+*.dat) takes all the files in the path with the extension .dat,
#here, in the "for file in files" the "file" has the whole path+name_extension

