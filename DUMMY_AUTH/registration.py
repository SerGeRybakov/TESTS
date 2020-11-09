import random
import string
from hashlib import sha256

from DUMMY_AUTH.database import DB


class NewUser(DB):
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._username = self._generate_username()
        self._password = self._generate_password()
        self._pass_hash = generate_hash(self._password)
        return self._create_user

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
        return

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


def generate_hash(password):
    return sha256(password.encode()).hexdigest()


if __name__ == '__main__':
    pass
