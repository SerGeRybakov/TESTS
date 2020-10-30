from pprint import pprint

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


def check_line(line):
    for i in line:
        if line.count(i) > 1:
            return False
    return True


def check_sudoku(grid):
    # выделяем строки
    for line in grid:
        if not check_line(line):
            return False

    # выделяем колонки
    for i in range(len(grid)):
        column = [line[i] for line in grid]
        if not check_line(column):
            return False

    # выделяем квадраты (3х3 по всей сетке с соответствующим шагом)
    square = []
    for line in grid[:3]:
        print(line)
        square.extend(line[:3])
    print()
    pprint(square)
    if not check_line(square):
        return False

    return True


print(check_sudoku(grid_true))
print()
print(check_sudoku(grid_false))


