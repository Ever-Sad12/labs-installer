import os
import time
import requests

def banner():
    cmd = 'cat banner.txt'
    os.system(cmd)

def home():
    print('[+] choose your lab [+]\n')
    print('             [1] DVWA')                                                  
    print('             [2] XSS (soon)')
    print('             [3] DVFU')
    print('             [4] BWAPP\n')


banner()
home()

cho = int(input('lab@localhost :: '))
if cho == 1:
    print('DVWA is installing')
    cmd = 'apt install git -y && git clone https://github.com/digininja/DVWA.git'
    os.system(cmd)
elif cho == 2:
    print('XSS is not include in this ver')
elif cho == 3:
    print('DVFU is installing')
    cmd = 'apt install git -y && git clone https://github.com/LunaM00n/File-Upload-Lab.git'
    os.system(cmd)
elif cho == 4:
    print('BWAPP is installing') 
    cmd = 'apt install git -y && git clone https://github.com/Ever-Sad12/bWAPP.git && unzip bWAPP.zip'
    os.system(cmd)
else:
    print('try later')
