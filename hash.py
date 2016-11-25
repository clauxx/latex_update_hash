import hashlib
import time
import subprocess
import sys

#checking if the hash for the file has changed
def check():
    global hash_1
    
    hash_2 = read_file()
        
    if(hash_1 != hash_2):
        subprocess.call("/home/chris/Documents/Python/latex_update_hash/convert.sh", shell=True)
        hash_1 = hash_2

#opening a file and creating the hash
def read_file():
    global file_dir

    fd = open(file_dir, "r")
    curr = fd.read()
    m = hashlib.md5()
    m.update(curr.encode('utf-8'))
    hash_file = m.digest()
    fd.close()
    return hash_file

global hash_1

#gets the directory of the file from the argument
args = list(sys.argv) 
file_dir = args[1]

#reads the file
hash_1 = read_file()

#execution part
while True:
    #update time
    time.sleep(1) 
    check()


