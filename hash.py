import hashlib
import time
import subprocess

def check():
    global hash_1
    
    hash_2 = read_file()
        
    print(hash_1)
    print(hash_2)

    if(hash_1 != hash_2):
        subprocess.call("convert.sh", shell=TrueP)
        hash_1 = hash_2


def read_file():

    fd = open("/home/clauxx/Documents/LaTeX documents/Paper_Auditing_1/main.tex", 'r')
    curr = fd.read()
    m = hashlib.md5()
    hash_file = m.digest()
    fd.close()
    return hash_file

global hash_1


hash_1 = read_file()

while True:
    time.sleep(3)
    check()
    


