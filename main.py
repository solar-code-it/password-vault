from auth import register,login
from vault import encrypt_file,decrypt_file

# User menu where user can choose what to do.
def user_menu(username, key, salt):
    while True:
        print("\nwelcome", username)
        print("1. View data / Add data.")
        print("2. Store data.")
        print("3. logout")

        choice = input("Choose an option: ")

        # Change file name here for both the decrypted file and none decrypted file.
        if choice == "1":
            decrypt_file("test.txt.enc", key)
        elif choice == "2":
            encrypt_file("test.txt", key, salt)
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("invalid option.")

# Login pannel.
while True:

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        result = login()

        if result is not None:
            username, key, salt = result
            user_menu(username, key, salt)
            
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
