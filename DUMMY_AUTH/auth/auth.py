from hashlib import sha256
from typing import NoReturn

from DUMMY_AUTH.auth.database import DB
from DUMMY_AUTH.auth.exceptions import LogOutException


class Auth(DB):
    """
To change your username print "username".
To change your password print "password".
To delete your account print "delete".
To return to the main screen print "quit".

    """
    def __init__(self, username, password, path=DB.path):
        super().__init__()
        self.db_path = path
        true_username = self._check_username(username)
        if true_username:
            self.username = username
            true_pass = self._check_pass(password)
            if true_pass:
                user_info = [x for x in [user for user in self.read_db(self.db_path) if user['username'] == self.username]][0]
                self.password = password
                self._hash_pass = user_info['pass_hash']
                self.name = user_info['name']
                self._surname = user_info['surname']
                self._id = user_info['id']
                print(f"\nWELCOME TO THE DARK SIDE!")
            else:
                raise ValueError("Wrong password")
        else:
            raise ValueError("Wrong username")

    def __str__(self):
        return self.name + " " + self._surname

    def __repr__(self):
        return f"{type(self).__name__}({self.username!r}, {self.password!r})"

    def _check_username(self, username):
        users = [user['username'] for user in self.read_db(self.db_path)]
        return username in users

    def _check_pass(self, password):
        hash = [x['pass_hash'] for x in [user for user in self.read_db(self.db_path) if user['username'] == self.username]][0]
        new_hash = sha256(password.encode()).hexdigest()
        return hash == new_hash

    def change_username(self):
        db = self.read_db(self.db_path)
        user_info = [x for x in [user for user in db if user['username'] == self.username]][0]
        nicks = [user['username'] for user in db]
        new_username = input('Input your new username: ').strip().lower()

        while new_username in nicks or not new_username:
            print(f'Username {new_username} is being used by another user.')
            new_username = input('Input another new username or "break" to keep the old one: ')
        if new_username == "break":
            return
        self.username = new_username
        db[db.index(user_info)].update({"username": self.username})
        self.write_db(db, file=self.db_path)
        return True

    def change_password(self):
        db = self.read_db(self.db_path)
        user_info = [x for x in [user for user in db if user['username'] == self.username]][0]

        new_pass = input('Input your new password (at least 8 symbols) or "break" to keep the old one: ')
        if new_pass != "break":
            while len(new_pass) < 8 or new_pass == "break":
                print("New password must contain at least 8 symbols")
                new_pass = input('Input your new password (at least 8 symbols) or "break" to keep the old one: ')
                if new_pass == "break":
                    return
        else:
            return

        repeat = input('Input your new password once more or "break" to keep the old one: ')
        if repeat == "break":
            return

        if new_pass != repeat:
            raise ValueError("New passwords don't match each other. No change was made.")

        self.password = new_pass

        from DUMMY_AUTH.auth.registration import generate_hash
        self._hash_pass = generate_hash(self.password)

        db[db.index(user_info)].update({"password": self.password, "pass_hash": self._hash_pass})
        self.write_db(db, self.db_path)
        return True

    def delete_account(self) -> None:
        yes = "yes"
        decision = input('Are you sure you want to delete the account? Input "YES" if so. ').strip().lower()
        if decision != yes:
            print("Delete operation was canceled by user.")
            return

        last_check = self._check_pass(input('Please, input your password: '))
        if not last_check:
            print("Wrong password. Delete operation was canceled. Try again.")
            return

        db = self.read_db(self.db_path)
        user_info = [x for x in [user for user in db if user['username'] == self.username]][0]
        db.pop(db.index(user_info))
        self.write_db(db, self.db_path)
        raise LogOutException()

    def log_out(self) -> NoReturn:
        raise LogOutException()


if __name__ == '__main__':
    pass
