# Library Imports
import os
from cryptography.fernet import Fernet


# method to load key from textfile
def load_key():
    with open("keyfile.txt", "rb") as key:
        secret_key = key.read()
        return secret_key


# method to ingest encrypted file contents and return decrypted contents
def decrypt(file_contents):
    key = load_key()
    f = Fernet(key)
    decrypted_contents = f.decrypt(file_contents)
    return decrypted_contents


print("Welcome to the ransomware decryptor\n The program will now find your files")
# finds the files
files = []  # list variable for storing the files we will encrypt

for file in os.listdir():
    if file == "main.py" or file == "decrypt.py" or file == "keyfile.txt":
        continue
    if os.path.isfile(file):
        files.append(file)



for file in files:
    with open(file, "rb") as current_file:
        contents = current_file.read()
    plaintext = decrypt(contents)
    with open(file, "wb") as current_file:
        current_file.write(plaintext)
    print(file, " successfully decrypted")
