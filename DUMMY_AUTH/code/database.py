import json
import os
from typing import Dict, List, Any

file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'auth_db.json'))


class DB:
    @staticmethod
    def _read_db() -> List[Dict[str, Any]]:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def _write_db(db: List[Dict[str, Any]]) -> None:
        with open(file, 'w', encoding='utf-8') as f:
            return json.dump(db, f)


if __name__ == '__main__':
    pass
