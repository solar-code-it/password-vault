import os
import hashlib
import json
import base64
from cryptography.fernet import Fernet

USER_DB_FILE = "users.encrypted.json"
KEY_FILE = ".key"

def get_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            os.chmod(KEY_FILE, 0o600)
            f.write(key)
        return key

encryption_key = get_or_create_key()
cipher = Fernet(encryption_key)

def load_users():
    try:
        with open(USER_DB_FILE, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    json_data = json.dumps(users, indent=4)
    encrypted_data = cipher.encrypt(json_data.encode())
    with open(USER_DB_FILE, 'wb') as file:
        os.chmod(USER_DB_FILE, 0o600)
        file.write(encrypted_data)

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
    "salt": base64.b64encode(salt).decode(),
    "hash": base64.b64encode(hashed).decode()
    }

    users = load_users()
    users[username] = user_data
    save_users(users)

def login():
    username = input("Username: ")
    password = input("Password: ").encode()

    users = load_users()

    if username not in users:
        print("Username or password is wrong.")
        return

    saved_salt = base64.b64decode(users[username]["salt"])
    saved_hash = base64.b64decode(users[username]["hash"])

    new_hash = hashlib.scrypt(
        password,
        salt=saved_salt,
        n=16384,
        r=8,
        p=1
    )

    if new_hash == saved_hash:
        print("Login successfull.")
    else:
        print("Username or password is wrong.")

action = input("login or register: ")

action = action.lower()

if action == "login":
    login()
else:
    register()