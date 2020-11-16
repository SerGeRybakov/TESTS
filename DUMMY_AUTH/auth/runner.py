from DUMMY_AUTH.auth.auth import Auth
from DUMMY_AUTH.auth.registration import NewUser
from DUMMY_AUTH.auth.exceptions import LogOutException


def register():
    name = input("To create a new user input your first name: ")
    surname = input("Input your surname: ")
    # name, surname = "Sir", "Name"
    return NewUser(name, surname)


def log_in():
    username = input("Input your username: ")
    password = input("Input your password: ")
    # username, password = "v_pupkin", "123456"
    user = Auth(username, password)

    commands = {
        "username": user.change_username,
        "password": user.change_password,
        "delete": user.delete_account,
        "quit": user.log_out,
    }
    print(user.__doc__)
    while True:
        com = input('Input your choice here: ')
        print()
        if com not in commands:
            print("Wrong command!")
            print(user.__doc__)
            continue

        try:
            commands[com]()
        except ValueError as e:
            print(str(e))
            print()
        except LogOutException:
            return


def main():
    """For register input 1
For log in input 2
For exit input 3
"""
    main_commands = {
        "1": register,
        "2": log_in,
        "3": None
    }

    while True:
        print(main.__doc__)
        com = input('Input your choice here: ')
        print()
        if com not in main_commands:
            print("Wrong command!")
            continue

        if com == "3":
            print("Bye!")
            return

        try:
            main_commands[com]()
        except ValueError as e:
            print(str(e))
            print()


if __name__ == '__main__':
    main()
