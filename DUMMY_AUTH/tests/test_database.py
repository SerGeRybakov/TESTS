import pytest

from DUMMY_AUTH.auth.database import DB


def test__read_db():
    db = DB.read_db()
    assert isinstance(db, list)
    for i in db:
        assert isinstance(i, dict)


def test__write_db():
    database = DB.read_db()
    new_user = {"new_dict": "new_dict"}
    database.append(new_user)

    try:
        DB.write_db(database)
        db = DB.read_db()
        assert new_user == db[-1]

    finally:
        db.pop(-1)
        DB.write_db(db)
        assert new_user not in DB.read_db()


if __name__ == '__main__':
    pytest.main()
