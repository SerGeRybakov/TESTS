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


def check_nums(line):
    for num in line:
        if line.count(num) > 1:
            return False
    return True


def check_sudoku(grid):
    # выделяем строки
    for line in grid:
        if not check_nums(line):
            return False

    # выделяем колонки
    for i in range(len(grid)):
        column = [line[i] for line in grid]
        if not check_nums(column):
            return False

    # выделяем квадраты (3х3 по всей сетке с соответствующим шагом)
    squares = []
    for i in range(len(grid))[::3]:
        x = 0
        while x <= 6:
            square = []
            for line in grid[i:i + 3]:
                square.extend(line[x:x + 3])
            squares.append(square)
            x += 3

    for square in squares:
        if not check_nums(square):
            return False
    return True


print(check_sudoku(grid_true))
print(check_sudoku(grid_false))
