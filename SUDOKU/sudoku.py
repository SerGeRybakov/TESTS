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


def check_nums(line):
    for num in line:
        if line.count(num) > 1:
            return False
    return True


def lines(sudoku):
    """выделяем строки"""
    for line in sudoku:
        yield line


def columns(sudoku):
    """выделяем колонки"""
    for i in range(len(sudoku)):
        yield [line[i] for line in sudoku]


def blocks(sudoku):
    """выделяем квадраты (3х3 по всей сетке с соответствующим шагом)"""
    squares = []
    for i in range(len(sudoku))[::3]:
        for j in range(0, 8, 3):
            square = []
            for line in sudoku[i:i + 3]:
                square.extend(line[j:j + 3])
            squares.append(square)

    yield from squares


def check_sudoku(grid):
    for line in lines(grid):
        if not check_nums(line):
            return False

    for column in columns(grid):
        if not check_nums(column):
            return False

    for square in blocks(grid):
        if not check_nums(square):
            return False
    return True


print(check_sudoku(grid_true))
print(check_sudoku(grid_false))
