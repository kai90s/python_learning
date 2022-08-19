from encrypt1 import Fernet
with open('mykey.key', 'rb') as mykey :
    key = mykey.read()

print(key)

f = Fernet(key)

with open('enc_grades.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_grades.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)