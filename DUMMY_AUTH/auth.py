import json
import random
import string
from hashlib import sha256
from sys import exit
from typing import Dict, List


class DB():
    def __init__(self):
        super().__init__()

    @staticmethod
    def _read_db() -> List[Dict]:
        with open('auth_db.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def _write_db(db: List[Dict]) -> None:
        with open('auth_db.json', 'w', encoding='utf-8') as f:
            return json.dump(db, f)


class NewUser(DB):
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._username = self._generate_username()
        self._password = self._generate_password()
        self._pass_hash = self._generate_hash()
        self._create_user

    @property
    def _create_user(self):
        db = self._read_db()
        id_num = max(user['id'] for user in db) + 1
        new_user = {
            "id": id_num,
            "username": self._username,
            "name": self._name,
            "surname": self._surname,
            "password": self._password,
            "pass_hash": self._pass_hash
        }
        db.append(new_user)
        self._write_db(db)
        print(f"""Your login: {self._username}
Your password: {self._password}. 
If you wish you can change both username and password when you're logged in.""")

    def _generate_username(self):
        username = self._name.lower()[0] + "_" + self._surname.lower()
        for user in self._read_db():
            if user['username'] == username:
                username += "1"

                return username
        return username

    @staticmethod
    def _generate_password():
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(8, 12)
        return ''.join(random.choice(chars) for _ in range(size))

    def _generate_hash(self):
        return sha256(self._password.encode()).hexdigest()


class Auth(DB):
    # FIXME: нужно как-то убрать сюда кусок из __init__, но я что-то не так делаю
    # def __new__(cls, user, passw):
    #     for user in cls._read_db():
    #         if user['username'] == user:
    #             raise ValueError(f"Username {user} is already in use.")
    #     return super(User).__init__(user, passw)

    def __init__(self, username, password):
        super().__init__()
        true_username = self.check_username(username)
        if true_username:
            self.username = username
            true_pass = self.check_pass(password)
            if true_pass:
                print("Welcome to the dark side!")
            else:
                raise ValueError("Wrong password")
        else:
            raise ValueError("Wrong username")

    def check_username(self, username):
        users = [user['username'] for user in self._read_db()]
        print(users)
        return True if username in users else False

    def check_pass(self, password):
        user_info = [x for x in [user for user in self._read_db() if user['username'] == self.username]][0]
        print(user_info)
        hash = sha256(password.encode()).hexdigest()
        return True if user_info['pass_hash'] == hash else False


def register():
    # name = input("To create a new user input your first name: ")
    # surname = input("Input your surname: ")
    name = 'Vasya'
    surname = "Pupkin"
    return NewUser(name, surname)


def log_in():
    # username = input("To create a new user input your first name: ")
    # password = input("Input your surname: ")
    username, password = "v_pupkin", "123456"
    user = Auth(username, password)


def main():
    """For register input 1
For log in input 2
For exit input 3"""
    commands = {
        "1": register,
        "2": log_in,
        "3": exit
    }
    print(main.__doc__)
    com = input('Input your choice here: ')
    while com not in commands:
        com = input('Input your choice here: ')
    commands[com]()


if __name__ == '__main__':
    main()
