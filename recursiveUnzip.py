# Written by Kair0s3
# Usage - Change the originalFile to the zip file you want to recursively unzip
#       - You may want to remove line 17 if your zip file doesn't require password
#       - PLZNOTE - You may want to modify the script in the case that some zip files may require password while some doesn't
# Reason for line 10, is mostly due to my project folder configurations

import os

from zipfile import ZipFile

originalFile = "INSERT ORIGINAL ZIPPED FILE HERE"
cwd = os.path.dirname(os.path.abspath(__file__))
file = cwd + f"\\{originalFile}"

while 1:
    try:
        z = ZipFile(file)
        z.setpassword(b"PASSWORD") #password to supply to unzip
        file = os.path.abspath(f"{file}\\..\\{originalFile[:-4]}\\")
        z.extractall(file)
    except:
        break
    cwdList = os.listdir(path=file)
    print (file + "\\" + str(cwdList))
    for i in cwdList:
        if "zip" in i:
            tmp = i
            break
        else:
            tmp = ""
    file = file + "\\" + tmp
    originalFile = tmp

for j in os.listdir(path=file):
    with open(f'{file}\\{j}') as f:
        print (f.read())
