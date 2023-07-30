import pyAesCrypt

password = input("Enter a password to encrypt a file: ")
file = "aescrypt_files/text.txt"
encrypted_file = f"{file}.aes"

# Encrypt file
pyAesCrypt.encryptFile(file, encrypted_file, password)

# Decrypt file
password = input("Enter a password to decrypt a file: ")

pyAesCrypt.decryptFile(encrypted_file, file, password)
