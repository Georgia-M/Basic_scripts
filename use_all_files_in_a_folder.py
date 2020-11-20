import os

thisdir = os.getcwd()

for r, d, f in os.walk('C:/Users/user/Desktop/test'):
    for file in f:
        if file.endswith(".pdb"):
            print(file)

#or


files = glob.glob(pdbs_path+'\\*.pdb')
#sort them by date
files.sort(key = os.path.getmtime, reverse=False)
for file in files:
    print(file)
