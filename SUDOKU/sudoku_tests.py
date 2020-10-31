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
    (grid_true, [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5]
    ]),
    (grid_false, [
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
     ),
])
def test_lines(sample, expected):
    lines = sudoku.lines(sample)

    for expected_line in expected:
        line = next(lines)
        assert line == expected_line


@pytest.mark.parametrize('sample, expected', [
    (grid_true, [
        [1, 4, 7, 2, 5, 8, 9, 3, 6],
        [2, 5, 8, 3, 6, 9, 1, 4, 7],
        [3, 6, 9, 4, 7, 1, 2, 5, 8],
        [4, 7, 1, 5, 8, 2, 3, 6, 9],
        [5, 8, 2, 6, 9, 3, 4, 7, 1],
        [6, 9, 3, 7, 1, 4, 5, 8, 2],
        [7, 1, 4, 8, 2, 5, 6, 9, 3],
        [8, 2, 5, 9, 3, 6, 7, 1, 4],
        [9, 3, 6, 1, 4, 7, 8, 2, 5]
    ]
     ),
    (grid_false, [
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
     ),
])
def test_columns(sample, expected):
    columns = sudoku.columns(sample)

    for expected_column in expected:
        column = next(columns)
        assert column == expected_column


@pytest.mark.parametrize('sample, expected', [
    (grid_true, [
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
     ),
    (grid_false, [
        [1, 2, 3, 2, 3, 4, 3, 4, 5],
        [4, 5, 6, 5, 6, 7, 6, 7, 8],
        [7, 8, 9, 8, 9, 1, 9, 1, 2],
        [4, 5, 6, 5, 6, 7, 6, 7, 8],
        [7, 8, 9, 8, 9, 1, 9, 1, 2],
        [1, 2, 3, 2, 3, 4, 3, 4, 5],
        [7, 8, 9, 8, 9, 1, 9, 1, 2],
        [1, 2, 3, 2, 3, 4, 3, 4, 5],
        [4, 5, 6, 5, 6, 7, 6, 7, 8],
    ]
     ),
])
def test_blocks(sample, expected):
    blocks = sudoku.blocks(sample)

    for expected_block in expected:
        block = next(blocks)
        assert block == expected_block


@pytest.mark.parametrize('sample, expected', [
    (grid_true, True),
    (grid_false, False),
])
def test_check_sudoku(sample, expected):
    assert expected == sudoku.check_sudoku(sample)


if __name__ == '__main__':
    pytest.main()
