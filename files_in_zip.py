'''work with files in a zip'''

from zipfile import ZipFile
import detetime

file_name = "C:User/user/Desktop/proteins.zip"

with ZipFile(file_name, 'r') as zip:
    for info in zip.infolist():
        print(info)

#info = all files inside the zip
