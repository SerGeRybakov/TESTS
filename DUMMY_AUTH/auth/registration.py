import random
import re
from hashlib import sha256
from string import printable, whitespace

from DUMMY_AUTH.auth.database import DB


class NewUser:
    def __init__(self, name: str, surname: str, path=DB.path):
        self.__path = path
        self.__db = DB.read_db(self.__path)
        self._name = name
        self._surname = surname
        self._username = self._generate_username(self._name, self._surname)
        self._password = self._generate_password()
        self._pass_hash = generate_hash(self._password)
        self._create_user()

    def _create_user(self):
        id_num = max(user['id'] for user in self.__db) + 1
        new_user = {
            "id": id_num,
            "username": self._username,
            "name": self._name,
            "surname": self._surname,
            "password": self._password,
            "pass_hash": self._pass_hash
        }

        self.__db.append(new_user)
        DB.write_db(self.__db, file=self.__path)
        print(f"""
Your username: {self._username}
Your password: {self._password}
You can change both username and password when you're logged in.""")

    def _generate_username(self, name, surname):
        username = name.lower()[0] + "_" + surname.lower()
        similar = [user['username'] for user in self.__db if username in user['username']]
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
