import string

def caesar(text,shift,alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[shift:]

shifted_alphabet = tuple(map(shift_alphabet,alphabets))
final_alphabet = ''.join(alphabets)
final_shifted_alphabet = ''.join(shifted_alphabets)
table = str.maketrans(final_alphabet,final_shifted_alphabet)
return text.translate(table)
plain_text="this is a new test, Hello World!"
print(caesar(plain_text,3,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))