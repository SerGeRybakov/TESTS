def check_line(line):
    for i in line:
        if line.count(i) > 1:
            return False
    return True


def check_column(column):
    for i in column:
        if column.count(i) > 1:
            return False
    return True


def check_square(line, column):

    for j in line[::3]:
        if line[::3][0] != column[::3][0]:
            return False
        if line[::3].count(line.index(j)) > 1:
            return False
        if column[::3].count(column.index(j)) > 1:
            return False
    return True
