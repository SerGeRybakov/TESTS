from random import randint
from SUDOKU import sudoku
import pytest


@pytest.mark.parametrize('sample', 'expected', [
    ([i for i in range(1, 10)], True),
    ([randint(1, 9) for i in range(1, 10)], False),
    # (,),
    # (,),
    # (,),
    # (,),
    # (,),
    # (,),
    # (,),
])
def test_check_line(sample, expected):
    assert expected == sudoku.check_line(sample)


if __name__ == '__main__':
    pytest.main()
