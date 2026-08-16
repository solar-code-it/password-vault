from auth import register,login

def user_menu(username):
    while True:
        print("\nwelcome", username)
        print("1. View data.")
        print("2. Add data.")
        print("3. logout")

        choice = input("Choose an option: ")

        if choice == "1":
            print ("viewing data")
        elif choice == "2":
            print ("adding data")
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
        username = login()

        if username:
            user_menu(username)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
