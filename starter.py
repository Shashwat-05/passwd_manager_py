# import getpass

# from Crypto.PublicKey import RSA
# from Crypto.Random import get_random_bytes
# from Crypto.Cipher import AES,PKCS1_OAEP 
# import os.path
# from keys_generator import generate_keys


# user = input('enter username or client name : ')
# passwd = getpass.getpass(prompt='enter the password : ')
# xtra_info = input('enter the description in one line : ')


# keys_exists = os.path.exists('pub_key_file')

# if not keys_exists:
#     print('no keys exists ... generating new keys!!')
#     generate_keys()
#     print('\nnew keys generated successfully...')


# f2 = open('pub_key_file','r')
# pub_file = f2.read()

# publicKeyReloaded = rsa.PublicKey.load_pkcs1(pub_file.encode('utf8')) 


# encoded_pass = passwd.encode('utf-8')
# f = open('')

# pub_key = RSA.import_key(open('pubKey.pem').read())
# session_key = get_random_bytes(16)

# cipher_ = PKCS1_OAEP.new(pub_key)
# enc_sess_key = cipher_.encrypt(session_key)

# cipher_aes = AES.new(session_key,AES.MODE_EAX)
# ciphertext,tag = cipher_aes.encrypt_and_digest(encoded_pass)
# enc_pass = rsa.encrypt(passwd.encode(),publicKeyReloaded)
# print('encrypted password successfully...')
# print('\nencrypted password : ',enc_pass)

# #will now contact to mdb server -> database == user_credentials

# #then will update the values as per the given info in the collection == [credentials[social,professional,personal,useless]]

# #another file will help to fetch a user credentials from the data base

# #also these passwords will be already encrypted with the best algorithms.

# #the database will have separate user login details as only for python script/tanet.

# #until then let's store it inside a file with yaml or json format.
# print('updating credentials ... \n\n')
# with open('local_credentials.yml','a') as file:
# 	file.write(f'\n{user}:\n password: {enc_pass}\n description: {xtra_info}\n')

# print('credentials updated...!!')



