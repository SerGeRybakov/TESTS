import tempfile
from shutil import copy2
from unittest.mock import patch

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
    return Auth('v_pupkin', '12345', path=mock_database)


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
    assert isinstance(login, str)
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
    assert isinstance(password, str)
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


@pytest.mark.parametrize('username', ['v_gupkin', "123456"])
def test_change_username(existing_user, mock_database, username):
    with patch('builtins.input', return_value=username):
        existing_user.change_username()
    assert Auth(username, "12345", mock_database)


def test_break_change_username(existing_user, mock_database):
    with patch('builtins.input', return_value='break'):
        assert not existing_user.change_username()
    with pytest.raises(ValueError):
        Auth("break", "12345", mock_database)


@pytest.mark.xfail
def test_change_username1(existing_user, capsys):
    with patch('builtins.input', side_effect=('i_isanov1', 'break')) as mock_input:
        out, err = capsys.readouterr()
        existing_user.change_username()
        mock_input.assert_called()
        assert out == f'Username i_isanov1 is being used by another user.'


if __name__ == '__main__':
    pytest.main()
