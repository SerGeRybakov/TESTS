import pytest

from DUMMY_AUTH.code.database import DB


def test__read_db():
    db = DB._read_db()
    assert isinstance(db, list)
    for i in db:
        assert isinstance(i, dict)


def test__write_db():
    database = DB._read_db()
    new_user = {"new_dict": "new_dict"}

    database.append(new_user)
    DB._write_db(database)

    db = DB._read_db()
    assert new_user == db[-1]

    db.pop(-1)
    DB._write_db(db)
    assert new_user not in DB._read_db()


if __name__ == '__main__':
    pytest.main()
