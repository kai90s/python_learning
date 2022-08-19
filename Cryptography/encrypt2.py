from encrypt1 import Fernet
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)