import sys
import hashlib
import os
path=sys.argv[1]

try:
    os.system("figlet -ct Virus Scanner")
except:
    os.system("sudo apt get install figlet")
    os.system("figlet -ct Virus Scanner")
#banner("GPCSSI Project")


abc=str(path)
print("File name: "+abc)
md5_hash = hashlib.md5()

a_file = open(abc, "rb")
content = a_file.read()
md5_hash.update(content)

digest = md5_hash.hexdigest()
print("\nMd5 hash of File: "+str(digest))
virus_def=open("database.txt","r")
file_not_read=False
print("\nScaning... ")
#hasher=hashlib.md5()
try:
    for line in virus_def:
        if digest== line.strip():
            print("\nInfected File")
            a=0
            break
        else:
            a=1
    if a==1:
        print("Clean")
except Exception as e:
    print(" could not read the file Error: {}".format(e))
print("Completed!")

