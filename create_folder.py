'''creating a folder'''
import os

path = 'C:/Users/user/Desktop/test'

try:
    os.mkdir(path)
except OSError:
    print("Creation of the folder failed")
else:
    print("Successfully created folder.")


#or just:
path = 'C:/Users/user/Desktop/test'
os.mkdir(path)
