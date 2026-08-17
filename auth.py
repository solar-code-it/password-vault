import hashlib
import os
import json

# Makes vault key.
def make_key(password, salt):
    return hashlib.scrypt(
        password,
        salt=salt,
        n=32768,
        r=8,
        p=1,
        dklen=32,
        maxmem=128 * 1024 * 1024
    )

# Registers user to user.json.
def register():
    username = input("Username: ")
    password = input("Password: ").encode()

    salt = os.urandom(16)

    hashed = hashlib.scrypt(
        password,
        salt=salt,
        n=32768,
        r=8,
        p=1,
        dklen=32,
        maxmem=128 * 1024 * 1024
    )

    user_data = {
    "salt": salt.hex(),
    "hash": hashed.hex()
    }

    try:
        with open ("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    users[username] = user_data

    with open  ("users.json", "w") as file:
        json.dump(users, file, indent=4)

    return password


# login system + makes vault incase there is no vault.
def login():
    username = input("Username: ")
    password = input("Password: ").encode()
    
    # Change file name here.
    if os.path.exists("test.txt.enc"):
        with open("test.txt.enc", "rb") as file:
            salt = file.read(16)
    else:
        salt = os.urandom(16)

        # Create vault file and save the salt.
        # Change vault name here.
        with open("test.txt.enc", "wb") as file:
            file.write(salt)

    key = make_key(password, salt)

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("no user file found")
        return

    if username not in users:
        print("Username or password is wrong.")
        return

    saved_salt = bytes.fromhex(users[username]["salt"])
    saved_hash = bytes.fromhex(users[username]["hash"])

    new_hash = hashlib.scrypt(
        password,
        salt=saved_salt,
        n=32768,
        r=8,
        p=1,
        dklen=32,
        maxmem=128 * 1024 * 1024
    )

    if new_hash == saved_hash:
        print("Login successfull.")
        return username, key, salt

    else:
        print("Username or password is wrong.")
        return None
