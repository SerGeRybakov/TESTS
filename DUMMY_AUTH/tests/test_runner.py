from unittest.mock import patch

import pytest

from DUMMY_AUTH.auth import runner
from DUMMY_AUTH.auth.registration import NewUser
from DUMMY_AUTH.tests.test_auth import Fixtures


# не запускать - меняет боевую базу
@pytest.mark.skip
class TestFunctions(Fixtures):
    @pytest.mark.skip
    @pytest.mark.parametrize('new_name', [
        ('John', 'Smith'),
        ('Valery', 'Pupkin'),
        ('John', 'Smith'),
    ])
    def test_register(self, mock_database, new_name):
        with patch('builtins.input', side_effect=new_name):
            assert isinstance(NewUser, runner.register())


if __name__ == '__main__':
    pytest.main()
