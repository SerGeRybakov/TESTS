import random
import re
from string import printable, whitespace
from hashlib import sha256

from DUMMY_AUTH.code.database import DB

db = DB._read_db()


class NewUser:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._username = self._generate_username(self._name, self._surname)
        self._password = self._generate_password()
        self._pass_hash = generate_hash(self._password)
        self._create_user

    @property
    def _create_user(self):
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
        DB._write_db(db)
        print(f"""
Your login: {self._username}
Your password: {self._password}
If you wish you can change both username and password when you're logged in.""")
        return

    @staticmethod
    def _generate_username(name, surname):
        username = name.lower()[0] + "_" + surname.lower()
        similar = [user['username'] for user in db if username in user['username']]
        if similar:
            num = [re.findall(r'\d+$', name)[0] for name in similar if re.search(r'\d+$', name)]
            if num:
                username += str(int(max(num)) + 1)
            else:
                username += "1"
        return username

    @staticmethod
    def _generate_password():
        chars = printable.replace(whitespace, '')
        size = random.randint(8, 12)
        return ''.join(random.choice(chars) for _ in range(size))


def generate_hash(password):
    return sha256(password.encode()).hexdigest()


if __name__ == '__main__':
    pass
