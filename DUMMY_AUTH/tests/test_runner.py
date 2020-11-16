from unittest.mock import patch

import pytest

from DUMMY_AUTH.auth import runner
from DUMMY_AUTH.auth.registration import NewUser
from DUMMY_AUTH.tests.test_auth import Fixtures


class TestFunctions(Fixtures):

    # тест бестолковый, т.к. не тестирует ничего, кроме подменённого объекта
    @pytest.mark.skip
    @pytest.mark.parametrize('new_name', [
        ('John', 'Smith'),
        ('Valery', 'Pupkin'),
        ('John', 'Smith'),
    ])
    def test_register(self, mock_database, new_name):
        with patch('DUMMY_AUTH.auth.runner.register',
                   return_value=NewUser(*new_name, mock_database)) as reg:
            assert isinstance(reg(), NewUser)


if __name__ == '__main__':
    pytest.main()
