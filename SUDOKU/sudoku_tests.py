from random import randint

import pytest

from SUDOKU import sudoku

grid_false = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

grid_true = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5]
]


@pytest.mark.parametrize('sample, expected', [
    (grid_true, True),
    (grid_false, False),
])
def test_check_line(sample, expected):
    assert expected == sudoku.check_line(sample)


# @pytest.mark.parametrize('sample, expected', [
#     ([i for i in range(1, 10)], True),
#     ([randint(1, 9) for i in range(1, 10)], False)
# ])
# def test_check_column(sample, expected):
#     assert expected == sudoku.check_column(sample)
#
#
# @pytest.mark.parametrize('line, column, expected', [
#     ([i for i in range(1, 10)], [i for i in range(1, 10)], True),
#     ([randint(1, 9) for i in range(1, 10)], [randint(1, 9) for i in range(1, 10)], False)
# ])
# def test_check_square(line, column, expected):
#     assert expected == sudoku.check_square(line, column)


if __name__ == '__main__':
    pytest.main()
