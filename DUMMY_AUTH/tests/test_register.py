import re
import string

import pytest

from DUMMY_AUTH.auth.database import DB
from DUMMY_AUTH.auth.registration import NewUser, generate_hash


@pytest.fixture()
def new_user():
    yield NewUser("~~new~~", "user")
    db = DB.read_db()
    users = [user for user in db if "~~new~~" == user['name']]
    for user in users:
        db.remove(user)
    DB.write_db(db)


@pytest.mark.parametrize("name, surname, expected", [
    ("Vova", "Pushkin", "v_pushkin"),
    ("Vova", "Pupkin", "v_pupkin1"),
    ("Ilya", "Isanov", "i_isanov2"),
    ("Ilya", "Ivanov", "i_ivanov11"),
])
def test_generate_username(name, surname, expected, new_user):
    username = new_user._generate_username(name, surname)
    assert username == expected


def test_generate_password(new_user):
    pass1 = new_user._generate_password()
    pass2 = new_user._generate_password()
    assert pass1 != pass2


def test_password_len(new_user):
    assert 8 <= len(new_user._generate_password()) <= 13


@pytest.mark.parametrize('chars', [
    f"[{string.ascii_uppercase}]+",
    f"[{string.ascii_lowercase}]+",
    f"[{string.digits}]+",
    f"[{string.punctuation}]+",
])
# FIXME: иногда валится, т.к. в самом методе нет чёткой обязанности
#  содержать все эти варианты одновременно
def test_chars_in_password(chars, new_user):
    password = new_user._generate_password()
    assert re.findall(chars, password)


@pytest.mark.parametrize("password, hash", [
    ('qwerty', '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5'),
    ('123456', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
    ('fjJUImop83?`msdnD0', '93d78f7df319e921751780158bfbcf56a6a58f92854d512f663177389272b8e0'),
])
def test_generate_hash(password, hash):
    result = generate_hash(password)
    assert hash == result


def test_create_user(new_user):
    assert new_user._username == DB.read_db()[-1]['username']


def test_create_user_output(capsys, new_user):
    out, err = capsys.readouterr()
    message = f"""
Your username: {new_user._username}
Your password: {new_user._password}
You can change both username and password when you're logged in."""

    assert out.rstrip() == message


if __name__ == '__main__':
    pytest.main()
