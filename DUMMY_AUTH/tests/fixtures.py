import tempfile
from shutil import copy2

import pytest

from DUMMY_AUTH.auth.auth import Auth
from DUMMY_AUTH.auth.database import DB
from DUMMY_AUTH.auth.registration import NewUser


class Fixtures:
    @pytest.fixture()
    def mock_database(self):
        with tempfile.NamedTemporaryFile() as file:
            file.close()
            copy2(DB.path, file.name)
            yield file.name

    @pytest.fixture()
    def existing_user(self, mock_database):
        return Auth('v_pupkin', '12345', path=mock_database)

    @pytest.fixture()
    def read_mock_db(self, mock_database):
        return DB.read_db(mock_database)

    @pytest.fixture()
    def new_user(self, mock_database):
        return NewUser("~~new~~", "user", mock_database)

