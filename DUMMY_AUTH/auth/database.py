import json
import os
from typing import Dict, List, Any


class DB:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'auth_db.json'))

    @staticmethod
    def read_db(file=path) -> List[Dict[str, Any]]:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def write_db(db: List[Dict[str, Any]], file=path) -> None:
        with open(file, 'w', encoding='utf-8') as f:
            return json.dump(db, f)


if __name__ == '__main__':
    pass
