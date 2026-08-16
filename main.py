from auth import register,login
from vault import encrypt_file,decrypt_file

def user_menu(username, password):
    while True:
        print("\nwelcome", username)
        print("1. View data.")
        print("2. Add data.")
        print("3. logout")

        choice = input("Choose an option: ")

        if choice == "1":
            encrypt_file("test.txt", password)
        elif choice == "2":
            decrypt_file("test.txt.enc", password)
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("invalid option.")


while True:

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        username, password = login()

        if username:
            user_menu(username, password)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
