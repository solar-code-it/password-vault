import hashlib
import os
import json

def register():
    username = input("Username: ")
    password = input("Password: ").encode()

    salt = os.urandom(16)

    hashed = hashlib.scrypt(
        password,
        salt=salt,
        n=16384,
        r=8,
        p=1
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

def login():
    username = input("Username: ")
    password = input("Password: ").encode()

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
        n=16384,
        r=8,
        p=1
    )

    if new_hash == saved_hash:
        print("Login successfull.")
        return username, password

    else:
        print("Username or password is wrong.")
        return None
