from getpass import getpass

import pyAesCrypt

password = getpass(prompt="Enter a password to encrypt a file: ")
file = "aescrypt_files/text.txt"
encrypted_file = f"{file}.aes"

# Encrypt file
pyAesCrypt.encryptFile(file, encrypted_file, password)

# Decrypt file
password = getpass(prompt="Enter a password to decrypt a file: ")

pyAesCrypt.decryptFile(encrypted_file, file, password)
