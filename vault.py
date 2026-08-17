from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Encrypts  text.
def encrypt_file(filename, key, salt):
    nonce = os.urandom(12)

    with open (filename, "rb") as file:
         data = file.read()

    encrypted = AESGCM(key).encrypt(nonce, data, None)

    with open(filename + ".enc", "wb") as file:
        file.write(salt)
        file.write(nonce)
        file.write(encrypted)

# Decrypts text.
def decrypt_file(filename, key):
    with open(filename, "rb") as file:
        salt = file.read(16)
        nonce = file.read(12)
        encrypted = file.read()

    data = AESGCM(key).decrypt(nonce, encrypted, None)

    output = filename.removesuffix(".enc")

    with open(output, "wb") as file:
        file.write(data)

