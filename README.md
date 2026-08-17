# Password Vault

A simple Python password vault with a login system and file encryption.

The project uses scrypt for password hashing/key derivation and AES-GCM for encrypting files. It is currently a small learning project focused on understanding authentication and encryption.

Project Status: Development is currently paused. This project is a learning/prototype project and is not intended for production use.

## Features

* User registration and login
* Password hashing with `scrypt`
* Random salts
* AES-GCM file encryption
* File decryption
* Simple command-line interface
* Configurable input/encrypted file names

## Requirements

* **Python**  preferably the latest stable version
* **cryptography**  install with `pip install cryptography`

## Getting Started

Clone the repository:

```bash
git clone https://github.com/solar-code-it/password-vault.git
cd password-vault
```

Install the required package:

```bash
pip install cryptography
```

Then run:

```bash
python main.py
```

## Before Using the Vault

**You need to manually create the original plaintext file that you want to encrypt.**

For example, the default configuration uses:

```text
test.txt
```

Create this file yourself in the project directory:

```text
password-vault/
├── test.txt
├── main.py
├── auth.py
└── vault.py
```

Put the data you want to encrypt inside `test.txt`.

### What happens when you encrypt?

When you choose the encryption option, the program reads:

```text
test.txt
```

and creates:

```text
test.txt.enc
```

The `.enc` file contains the encrypted data along with the salt and nonce required for decryption.

### What happens when you decrypt?

When you decrypt:

```text
test.txt.enc
```

The program decrypts the encrypted file and writes the decrypted data back to:

```text
test.txt
```

The original `test.txt` file must be created manually before encrypting. When the encrypted file is decrypted, the plaintext data is written back to `test.txt`.


The decrypted file is therefore written back as the original filename.

> **Important:** The original plaintext file must exist before you can encrypt it. The program does not create the initial plaintext file for you.

## Changing the File Names

You can change which files the program uses by editing the filenames in `main.py` and `vault.py`.

By default, the program uses:

```python
decrypt_file("test.txt.enc", key)
```

and:

```python
encrypt_file("test.txt", key, salt)
```

If you want to use different filenames, change them in both places.

For example:

```python
decrypt_file("my_secrets.txt.enc", key)
```

and:

```python
encrypt_file("my_secrets.txt", key, salt)
```

You must manually create the original plaintext file:

```text
my_secrets.txt
```

before using the encryption option.

The encrypted file:

```text
my_secrets.txt.enc
```

is created automatically **when you log in for the first time**.

When the encrypted file is decrypted, the decrypted data is written back to:

```text
my_secrets.txt
```


## How Authentication Works

When registering, the program:

1. Asks for a username and password.
2. Generates a random 16-byte salt.
3. Uses `scrypt` to derive a 32-byte password hash.
4. Stores the salt and hash in `users.json`.

`users.json` is created automatically if it does not already exist.

During login, the stored salt is used to verify the password. The vault encryption key is also derived from the password using `scrypt`.

## Encryption

The vault uses **AES-GCM** for file encryption.

The encryption process generates:

* A random nonce
* A salt
* A key derived from the user's password
* Encrypted file contents

The resulting encrypted file has the `.enc` extension.

## Project Structure

```text
password-vault/
├── main.py        # Main CLI and file names
├── auth.py        # Registration and login
├── vault.py       # Encryption and decryption
├── users.json     # User authentication data
├── test.txt       # Plaintext file you create
└── test.txt.enc   # Encrypted file created by the program
```

`test.txt` and `test.txt.enc` are examples based on the current default configuration. You can change the filenames in `main.py`.

## Usage

Run:

```bash
python main.py
```

### Main menu

```text
1. Register
2. Login
3. Exit
```

### After logging in

```text
1. View data / Add data.
2. Store data.
3. logout
```

**Option 1** decrypts the encrypted file and lets you add stuff to the .text to be encrypted.

**Option 2** encrypts the plaintext file.

**Option 3** logs out.

## Security Warning

This is currently a **learning/prototype project**, not a production-ready password manager.

Some things that should be improved before using it for real sensitive data include:

* Secure password input using `getpass`
* Better authentication handling
* Proper password-entry management
* Secure deletion of plaintext files
* Better error handling
* Automated security tests
* Protection against file tampering
* More robust vault management

Never commit your real `users.json`, plaintext files, or encrypted vault files containing sensitive information to a public repository.

## Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a branch.
3. Make your changes.
4. Test them.
5. Open a pull request.

