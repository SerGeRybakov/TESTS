from unittest.mock import patch

import pytest

from DUMMY_AUTH.auth import runner
from DUMMY_AUTH.auth.database import DB
from DUMMY_AUTH.auth.registration import NewUser
from DUMMY_AUTH.tests.test_auth import Fixtures


class TestFunctions(Fixtures):
    welcome = """
WELCOME TO THE DARK SIDE!

To change your username print "username".
To change your password print "password".
To delete your account print "delete".
To return to the main screen print "quit".\n\n\n\n"""

    # тест бестолковый, т.к. не тестирует ничего, кроме подменённого объекта
    @pytest.mark.skip
    @pytest.mark.parametrize('new_name', [
        ('John', 'Smith'),
        ('Valery', 'Pupkin'),
        ('John', 'Smith'),
    ])
    def test_register_mock(self, mock_database, new_name):
        with patch('DUMMY_AUTH.auth.runner.register',
                   return_value=NewUser(*new_name, mock_database)) as reg:
            assert isinstance(reg(), NewUser)

    @pytest.mark.parametrize('new_name, expected_username', [
        (('John', 'Smith'), "j_smith"),
        (('Valery', 'Pupkin'), "v_pupkin1"),
        (('Ivan', 'Ivanov'), "i_ivanov11"),
    ])
    def test_register(self, new_name, expected_username):
        with patch('builtins.input', side_effect=new_name):
            user = runner.register()
            try:
                assert isinstance(user, NewUser)
                assert user._username == expected_username
            finally:
                db = DB.read_db()
                user = [user_ for user_ in db if expected_username == user_['username']][0]
                db.remove(user)
                DB.write_db(db)

    @pytest.mark.parametrize('inputs, message', [
        (('i_ivanov', 'abcde', 'username', 'break', 'quit'), welcome + 'Your username was not changed'),
        (('i_ivanov10', '123456', 'password', 'break', 'quit'), welcome + 'Your password was not changed'),
        (('n_johnson', 'qwerty', 'delete', 'break', 'quit'), welcome + "Delete operation was canceled by user."),
        (('n_johnson', 'qwerty', 'quit'), welcome.rstrip()),
    ])
    def test_log_in_username(self, inputs, message, mock_database, capsys):
        with patch('builtins.input', side_effect=inputs):
            runner.log_in()
            out, err = capsys.readouterr()
            assert out.rstrip() == message


if __name__ == '__main__':
    pytest.main()
