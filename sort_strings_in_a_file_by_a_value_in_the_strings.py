#sort the files by the deviation value

#the path of the file that we want to sort by a specific value
unsorted_file_path = folder_path+'/list_results.dat'

#we split the strings in the file after every "space" 
#here, the value by which we want to sort the strings is the second "word" (the word after the first "space") and it is float
sorted_lines = sorted((open(unsorted_file_path)).readlines(), key=lambda line: float(line.split(' ')[1]))

#write the sorted_lines inside the same file 
sorted_file = open(unsorted_file_path, 'w+')
for line in sorted_lines:
    n += 1
    string_n = str(n)
    sorted_file.write(string_n+') '+line)

sorted_file.close()
