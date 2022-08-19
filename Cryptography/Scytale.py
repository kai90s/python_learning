import cryptography as ciphertext
plaintext = "No good deed will go unpunished"
key=8
ciphertext=[''] * key

for column in range(key):
    pointer = column

    while pointer<len(plaintext):
        ciphertext[column]+=plaintext[pointer]

        pointer+=key

    print(''.join(ciphertext))