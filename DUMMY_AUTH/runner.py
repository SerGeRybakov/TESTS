from DUMMY_AUTH.auth import Auth
from DUMMY_AUTH.registration import NewUser


def register():
    # name = input("To create a new user input your first name: ")
    # surname = input("Input your surname: ")
    name = 'Sir'
    surname = "Name"
    return NewUser(name, surname)


def log_in():
    username = input("To create a new user input your first name: ")
    password = input("Input your surname: ")
    # username, password = "v_pupkin", "123456"
    user = Auth(username, password)


def main():
    """For register input 1
For log in input 2
For exit input 3
"""
    commands = {
        "1": register,
        "2": log_in,
        "3": exit
    }
    print(main.__doc__)
    com = input('Input your choice here: ')
    print()
    while com not in commands:
        com = input('Input your choice here: ')
        print()
    try:
        commands[com]()
    except ValueError as e:
        print(str(e))
        print()
        return


if __name__ == '__main__':
    while True:
        main()
