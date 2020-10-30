from random import randint


def check_line(line):
    for i in line:
        if line.count(i) == 1:
            return True
        return False


print(check_line([randint(1, 9) for i in range(1, 10)]))
print(check_line([i for i in range(1, 10)]))
