from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import hashlib

def make_key(password, salt):
    return hashlib.scrypt(
        password,
        salt=salt,
        n=16384,
        r=8,
        p=1,
        dklen=32
    )

def encrypt_file(filename, password):
    print(password)
    salt= os.urandom(16)
    key = make_key(password, salt)

    nonce = os.urandom(12)

    with open (filename, "rb") as file:
         data = file.read()

    encrypted = AESGCM(key).encrypt(nonce, data, None)

    with open(filename + ".enc", "wb") as file:
        file.write(salt)
        file.write(nonce)
        file.write(encrypted)

    
def decrypt_file(filename, password):
    with open(filename, "rb") as file:
        salt = file.read(16)
        nonce = file.read(12)
        encrypted = file.read()

    key = make_key(password, salt)

    data = AESGCM(key).decrypt(nonce, encrypted, None)

    output = filename.removesuffix(".enc")

    with open(output, "wb") as file:
        file.write(data)

