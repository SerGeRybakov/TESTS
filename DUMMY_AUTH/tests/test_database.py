import tempfile

import pytest

from DUMMY_AUTH.auth.database import DB


def test__read_db():
    db = DB.read_db()
    assert isinstance(db, list)
    for i in db:
        assert isinstance(i, dict)


def test__write_db():
    database = []
    new_user = {"new_dict": "new_dict"}
    database.append(new_user)

    with tempfile.NamedTemporaryFile() as file:
        file.close()
        DB.write_db(database, file=file.name)
        db = DB.read_db(file.name)
        assert new_user == db[-1]


if __name__ == '__main__':
    pytest.main()
