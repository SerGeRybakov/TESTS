from unittest.mock import patch

import pytest

from DUMMY_AUTH.auth.auth import Auth
from DUMMY_AUTH.tests.fixtures import Fixtures


class TestMagic(Fixtures):
    def test_init_output(self, capsys, existing_user):
        out, err = capsys.readouterr()
        assert out.rstrip() == f"\nwelcome to the dark side!".upper()

    @pytest.mark.parametrize('login', [
        '',
        'v_pukin',
        'v_pupkin'.upper(),
        'V_pupkin',
    ])
    def test_init_wrong_username(self, login):
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
    def test_init_wrong_password(self, password):
        assert isinstance(password, str)
        with pytest.raises(ValueError, match="Wrong password"):
            Auth('v_pupkin', password)

    def test_str(self, existing_user):
        assert str(existing_user) == "Vasya Pupkin"

    def test_repr(self, existing_user):
        assert repr(existing_user) == "Auth('v_pupkin', '12345')"


class TestChecks(Fixtures):
    @pytest.mark.parametrize('login, expected', [
        ('v_pupkin', True),
        ('a_pushkin', False)
    ])
    def test__check_username(self, existing_user, login, expected):
        assert existing_user._check_username(login) == expected

    @pytest.mark.parametrize('password, expected', [
        ('12345', True),
        ('123456', False)
    ])
    def test__check_password(self, existing_user, password, expected):
        assert existing_user._check_pass(password) == expected


class TestUsername(Fixtures):

    @pytest.mark.parametrize('username', ['v_gupkin', "123456"])
    def test_change_username(self, existing_user, mock_database, username):
        with patch('builtins.input', return_value=username):
            assert existing_user.change_username()
        assert Auth(username, "12345", mock_database).username == username

    def test_break_change_username(self, existing_user, mock_database):
        with patch('builtins.input', return_value='break'):
            assert not existing_user.change_username()
        with pytest.raises(ValueError, match='Wrong username'):
            Auth("break", "12345", mock_database)

    @pytest.mark.parametrize('login', [
        ('i_isanov1', 'break'),
        ('i_ivanov10', 'i_isanov10')
    ])
    def test_reserved_name_change_username(self, existing_user, capsys, login):
        with patch('builtins.input', side_effect=login) as mock_input:
            existing_user.change_username()
            out, err = capsys.readouterr()
            mock_input.assert_called()
            assert out.rstrip() == f'Username {login[0]} is being used by another user.'


class TestPassword(Fixtures):
    @pytest.mark.parametrize('password', [
        ('01234567', "01234567"),
        ('sejKDeS!3-', 'sejKDeS!3-')
    ])
    def test_change_password(self, existing_user, mock_database, password):
        with patch('builtins.input', side_effect=password):
            assert existing_user.change_password()
        assert Auth('v_pupkin', password[0], mock_database)

    @pytest.mark.parametrize('password', [
        ('01234567', "break"),
        ('break',)
    ])
    def test_break_change_password(self, existing_user, mock_database, password):
        with patch('builtins.input', side_effect=password):
            assert not existing_user.change_password()
        with pytest.raises(ValueError, match='Wrong password'):
            Auth("v_pupkin", "break", mock_database)

    @pytest.mark.parametrize('password', [
        ('01234567', "12345678"),
        ('aAbBcCdD', "aAbBcCDD"),
        ('aAbBcCdD', " "),
        ('aAbBcCdD', "")
    ])
    def test_incorrect_change_password(self, existing_user, mock_database, password):
        with pytest.raises(ValueError, match="New passwords don't match each other. No change was made."):
            with patch('builtins.input', side_effect=password):
                existing_user.change_password()

    @pytest.mark.parametrize('password', [
        ('3245', '012345678', 'break'),
        ('aAbBdD', "aAbBcCDD", "aAbBcCDD")
    ])
    def test_incorrect_len_change_password(self, existing_user, mock_database, password, capsys):
        with patch('builtins.input', side_effect=password):
            existing_user.change_password()
            out, err = capsys.readouterr()
            assert out.rstrip() == "New password must contain at least 8 symbols"


class TestDelete(Fixtures):
    @pytest.mark.parametrize('answer', [
        ('yes', '12345'),
        ('Yes', '12345'),
        ('YEs', '12345'),
        ('YES', '12345'),
        ('yEs', '12345'),
        ('yES', '12345'),
        ('yeS', '12345'),
    ])
    def test_delete_account(self, existing_user, answer):
        with pytest.raises(SystemExit):
            with patch('builtins.input', side_effect=answer):
                existing_user.delete_account()

    @pytest.mark.parametrize('answer', [
        ('yes', '123456'),
        ('Yes', ''),
        ('YEs', ' '),
        ('YES', '54321'),
        ('yEs', '0'),
        ('yES', 'abcdef'),
        ('yeS', 'IKJHDfksdfgoijhkndsv;iklhfdg'),
    ])
    def test_wrong_password_delete_account(self, existing_user, read_mock_db, answer):
        with pytest.raises(ValueError, match="Wrong password. Delete operation was canceled. Try again."):
            with patch('builtins.input', side_effect=answer):
                existing_user.delete_account()
        assert read_mock_db[0]['username'] == existing_user.username

    @pytest.mark.parametrize('answer', [
        '', ' ', 'no', '1', '0', '[]', '{}'
    ])
    def test_cancel_delete_account(self, existing_user, answer, capsys):
        with patch('builtins.input', return_value=answer):
            existing_user.delete_account()
            out, err = capsys.readouterr()
            assert out.rstrip() == "Delete operation was canceled by user."


if __name__ == '__main__':
    pytest.main()
