import pytest

from SUDOKU import sudoku

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

grid_false = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 5, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]

grid_false1 = [
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

grid_false2 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
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
        [5, 6, 7, 8, 5, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
     ),
])
def test_lines(sample, expected):
    lines = sudoku.lines(sample)

    for line, expected_line in zip(lines, expected):
        assert line == expected_line

    with pytest.raises(StopIteration):
        next(lines)


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
        [5, 6, 7, 8, 5, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
     ),
])
def test_columns(sample, expected):
    columns = sudoku.columns(sample)
    for column, expected_column in zip(columns, expected):
        assert column == expected_column

    with pytest.raises(StopIteration):
        next(columns)


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
        [7, 8, 9, 8, 5, 1, 9, 1, 2],
        [1, 2, 3, 2, 3, 4, 3, 4, 5],
        [7, 8, 9, 8, 9, 1, 9, 1, 2],
        [1, 2, 3, 2, 3, 4, 3, 4, 5],
        [4, 5, 6, 5, 6, 7, 6, 7, 8],
    ]
     ),
])
def test_blocks(sample, expected):
    blocks = sudoku.blocks(sample)
    for block, expected_block in zip(blocks, expected):
        assert block == expected_block

    with pytest.raises(StopIteration):
        next(blocks)


@pytest.mark.parametrize('sample, expected', [
    (grid_true, True),
    (grid_false, False),
    (grid_false1, False),
    (grid_false2, False),
])
def test_check_sudoku(sample, expected):
    assert expected == sudoku.check_sudoku(sample)


if __name__ == '__main__':
    pytest.main()
