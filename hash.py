import hashlib
import time
import subprocess

def check():
    global hash_1
    
    hash_2 = read_file()
        
    if(hash_1 != hash_2):
        subprocess.call("/home/chris/Documents/Python/latex_update_hash/convert.sh", shell=True)
        hash_1 = hash_2


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

file_dir = "/home/chris/Documents/LaTeX_documents/paper_auditing_1/main.tex"

hash_1 = read_file()

while True:
    time.sleep(3)
    check()
    


