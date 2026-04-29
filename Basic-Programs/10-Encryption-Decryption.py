import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(char)
key = chars.copy()

random.shuffle(key) 

#Encryption

NormalText = input("Enter a message to encrypt: ")
CypheredText = ""

for x in NormalText:
    index = chars.index(x)
    CypheredText += key[index]

print(f"Original message: {NormalText}")
print(f"Encrypted message: {CypheredText}")

#Decryption

CypheredText = input("Enter a message to Decrypt: ")
NormalText = ""

for x in CypheredText:
    index = key.index(x)
    NormalText += chars[index]

print(f"Encrypted message: {CypheredText}")
print(f"Original message: {NormalText}")
