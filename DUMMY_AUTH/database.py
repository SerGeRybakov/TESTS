import json
from typing import Dict, List


class DB:
    def __init__(self):
        super().__init__()

    @staticmethod
    def _read_db() -> List[Dict]:
        with open('auth_db.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def _write_db(db: List[Dict]) -> None:
        with open('auth_db.json', 'w', encoding='utf-8') as f:
            return json.dump(db, f)


if __name__ == '__main__':
    pass
