from DUMMY_AUTH.auth.auth import Auth
from DUMMY_AUTH.auth.registration import NewUser


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
    if user:
        commands = {
            "username": user.change_username,
            "password": user.change_password,
            "delete": user.delete_account,
            "quit": None
        }
        print(user.__doc__)
        com = input('Input your choice here: ')
        print()
        while com != 'quit':
            while com not in commands:
                print("Wrong command!")
                print(user.__doc__)
                com = input('Input your choice here: ')
                print()
            if com != "quit":
                try:
                    commands[com]()
                except ValueError as e:
                    print(str(e))
                    print()
                finally:
                    com = ""
            else:
                return


def main():
    """For register input 1
For log in input 2
For exit input 3
"""
    main_commands = {
        "1": register,
        "2": log_in,
        "3": exit
    }

    print(main.__doc__)
    com = input('Input your choice here: ')
    print()
    while com not in main_commands:
        print("Wrong command!")
        print(main.__doc__)
        com = input('Input your choice here: ')
        print()
    try:
        main_commands[com]()
    except ValueError as e:
        print(str(e))
        print()
    return


if __name__ == '__main__':
    while True:
        main()
