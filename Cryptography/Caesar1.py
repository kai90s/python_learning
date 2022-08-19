import string
import alphabet as alphabet

plain_text="hello world"
shift = 3
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[shift:]
table = str.maketrans(alphabet,shifted)
encrypted = plain_text
print(encrypted)