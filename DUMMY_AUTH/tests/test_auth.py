import tempfile
from shutil import copy2

import pytest

from DUMMY_AUTH.auth.auth import Auth
from DUMMY_AUTH.auth.database import DB


@pytest.fixture()
def mock_database():
    with tempfile.NamedTemporaryFile() as file:
        file.close()
        copy2(DB.path, file.name)
        yield file.name


@pytest.fixture()
def existing_user(mock_database):
    return Auth('v_pupkin', '12345', mock_database)


@pytest.fixture()
def read_mock_db(mock_database):
    return DB.read_db(mock_database)


def test_init_output(capsys, existing_user):
    out, err = capsys.readouterr()
    assert out.rstrip() == f"\nwelcome to the dark side!".upper()


@pytest.mark.parametrize('login', [
    '',
    'v_pukin',
    'v_pupkin'.upper(),
    'V_pupkin',
])
def test_init_wrong_username(login):
    with pytest.raises(ValueError, match="Wrong username"):
        Auth(login, '12345')


@pytest.mark.parametrize('password', [
    '',
    '1',
    '123',
    '12346',
    '54321',
    'v_pupkin',
    '-12345'
])
def test_init_wrong_password(password):
    with pytest.raises(ValueError, match="Wrong password"):
        Auth('v_pupkin', password)


def test_str(existing_user):
    assert str(existing_user) == "Vasya Pupkin"


def test_repr(existing_user):
    assert repr(existing_user) == "Auth('v_pupkin', '12345')"


@pytest.mark.parametrize('login, expected', [
    ('v_pupkin', True),
    ('a_pushkin', False)
])
def test__check_username(existing_user, login, expected):
    assert existing_user._check_username(login) == expected


@pytest.mark.parametrize('password, expected', [
    ('12345', True),
    ('123456', False)
])
def test__check_password(existing_user, password, expected):
    assert existing_user._check_pass(password) == expected


if __name__ == '__main__':
    pytest.main()
