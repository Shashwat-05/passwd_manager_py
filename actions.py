import sys
from cryptography.fernet import Fernet
import getpass
from os.path import exists
import yaml
from os import system

def clean_screen():
    try:
        system('clear')
    except:
        system('cls')

def key_generator():
    key = Fernet.generate_key()
    with open("refKey.txt", "wb") as f:
        f.write(key)
    return key

def credentials_feeder():
    print()
    user = input('enter username or client name : ')
    passwd = getpass.getpass(prompt='enter the password : ')
    xtra_info = input('enter the description in one line : ')

    if  exists('refKey.txt'):
        with open('refKey.txt') as f:
            key = ''.join(f.readlines())
            key = bytes(key,'utf-8')
        
    else:
        key = key_generator()


    refKey = Fernet(key)
    mypwdbyt = bytes(passwd, 'utf-8') 
    encryptedPWD = refKey.encrypt(mypwdbyt)

    print('updating credentials ... \n\n')
    with open('local_credentials.yml','a') as file:
        file.write(f'\n{user}:\n password: {encryptedPWD}\n description: {xtra_info}\n')
    print('credentials updated...!!')


def pass_fetcher():
    if exists('refKey.txt'):
        user = input('enter the user\'s password to fetch : ')

        with open(r'local_credentials.yml') as f:
            l = yaml.load(f, Loader=yaml.FullLoader)
            en_pass = l[user]['password']
            en_pass = en_pass[2:-1]
            en_pass_b = bytes(en_pass,'utf-8')
            details = l[user]['description']

        with open('refKey.txt') as f:
            refkey = ''.join(f.readlines())
            refkey_bytes = bytes(refkey,'utf-8')

        keyy = Fernet(refkey_bytes)
        password = keyy.decrypt(en_pass_b)
        
        print()
        print(f'''YOUR CREDENTIALS!!
user: {user}
password: {password.decode()}
description: {details}''')
        print()

    else:
        print('no private key exists to decrypt the password !!')