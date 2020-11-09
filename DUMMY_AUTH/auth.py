from hashlib import sha256

from DUMMY_AUTH.database import DB


class DataUser:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, *args, **kwargs):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

    def __del__(self):
        del self._name


class Auth(DB):
    username = DataUser()
    password = DataUser()
    _name = DataUser()
    surname = DataUser()
    _hash_pass = DataUser()

    def __init__(self, username, password):
        super().__init__()
        true_username = self._check_username(username)
        if true_username:
            self.username = username
            true_pass = self._check_pass(password)
            if true_pass:
                self.password = password
                self._hash_pass = true_pass[0]
                self.name = true_pass[1]
                self.surname = true_pass[2]
                self.id = true_pass[3]
                print("Welcome to the dark side!")
            else:
                raise ValueError("Wrong password")
        else:
            raise ValueError("Wrong username")

    def __str__(self):
        return self.name + self.surname

    def __repr__(self):
        return f"{type(self).__name__}({self.username!r}, {self.password!r})"

    def _check_username(self, username):
        users = [user['username'] for user in self._read_db()]
        return True if username in users else False

    def _check_pass(self, password):
        user_info = [x for x in [user for user in self._read_db() if user['username'] == self.username]][0]

        hash = sha256(password.encode()).hexdigest()
        if user_info['pass_hash'] == hash:
            return user_info['pass_hash'], user_info['name'], user_info['surname'], user_info['id']
        return False

    def change_username(self):
        db = self._read_db()
        user_info = [x for x in [user for user in db if user['username'] == self.username]][0]
        nicks = [user['username'] for user in db]
        new_username = input('Input your new username: ')

        while new_username in nicks:
            print(f'Username {new_username} is being used by another user.')
            new_username = input('Input another new username or "break" to keep the old one: ')
            if new_username == "break":
                return
        self.username = new_username
        db[db.index(user_info)].update({"username": self.username})
        self._write_db(db)
        return

    def change_password(self):
        db = self._read_db()
        user_info = [x for x in [user for user in db if user['username'] == self.username]][0]
        new_pass = input('Input your new password: ')
        repeat = input('Input your new password once more: ')
        if new_pass != repeat:
            raise ValueError("New passwords didn't match each other")

        self.password = new_pass

        from DUMMY_AUTH.registration import generate_hash
        self._hash_pass = generate_hash(self.password)

        db[db.index(user_info)].update({"password": self.password, "hash_pass": self._hash_pass})
        self._write_db(db)
        return

    def delete_account(self):
        yes = "yes"
        decision = input('Are you sure you want to delete the account? Print "YES" if so.').lower()
        if decision == yes:
            last_check = self._check_pass(input('Please, input your password: '))
            if last_check:
                db = self._read_db()
                user_info = [x for x in [user for user in db if user['username'] == self.username]][0]
                db.pop(db.index(user_info))
                del self.username
                del self.password
                del self._hash_pass
                del self.name
                del self.surname
                del self.id
                exit()


if __name__ == '__main__':
    username, password = "v_pupkin", "12345"
    user = Auth(username, password)
    print(user.id)
    user.id = 2
    print(user.id)
    user.change_username()
