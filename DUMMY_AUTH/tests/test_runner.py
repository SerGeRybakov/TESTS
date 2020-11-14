from unittest.mock import patch

import pytest

from DUMMY_AUTH.auth import runner
from DUMMY_AUTH.tests.test_auth import Fixtures

class TestFunctions(Fixtures):
    @pytest.mark.parametrize('new_user', [('John','Smith'),

    ]
    def test_register(self, existing_user, mock_database,):
        with patch('builtins.input', )
