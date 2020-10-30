from random import randint
from SUDOKU import sudoku
import pytest


@pytest.mark.parametrize('sample, expected', [
    ([i for i in range(1, 10)], True),
    ([randint(1, 9) for i in range(1, 10)], False),
])
def test_check_line(sample, expected):
    assert expected == sudoku.check_line(sample)


@pytest.mark.parametrize('sample, expected', [
    ([i for i in range(1, 10)], True),
    ([randint(1, 9) for i in range(1, 10)], False)
])
def test_check_column(sample, expected):
    assert expected == sudoku.check_column(sample)

@pytest.mark.parametrize('line, column, expected', [
    ([i for i in range(1, 10)], [i for i in range(1, 10)], True),
    ([randint(1, 9) for i in range(1, 10)], [randint(1, 9) for i in range(1, 10)], False)
])
def test_check_square(line, column, expected):
    assert expected == sudoku.check_square(line, column)


if __name__ == '__main__':
    pytest.main()
