"""Есть функция, на вход которой поступает произвольное количество отсортированных списков.
Функция должна слить эти списки в один отсортированный список.
Использовать sort или sorted само собой нельзя."""
from random import randint


def get_min_element(args):
    return min(min(args))


def create_new_sorted_list(args, min_element):
    new_lst = []
    for lst in args:
        if min_element in lst:
            new_lst.extend(lst)
            args.remove(lst)
            return new_lst, args


def insert_in_place(new_list, new_element):
    for element in new_list:
        if element >= new_element:
            new_list.insert(new_list.index(element), new_element)
            return new_list


def sort_elements(new_lst, next_list):
    for new_element in next_list:
        if new_element > new_lst[-1]:
            new_lst.extend(next_list[next_list.index(new_element)::])
            return new_lst
        if new_element in new_lst:
            new_lst.insert(new_lst.index(new_element), new_element)
        else:
            insert_in_place(new_lst, new_element)
    return new_lst


def main(test_list):
    min_element = get_min_element(test_list)
    new_list, args_lst = create_new_sorted_list(test_list, min_element)
    for lst in args_lst:
        sort_elements(new_list, lst)
    return new_list


if __name__ == '__main__':
    a = sorted([randint(x, 10) for x in range(10)])
    a1 = sorted([randint(x, 10) for x in range(10)])
    b = sorted([randint(x, 50) for x in range(50)])
    b1 = sorted([randint(x, 50) for x in range(50)])
    c = sorted([randint(x, 100) for x in range(100)])
    c1 = sorted([randint(x, 100) for x in range(100)])
    d = sorted([randint(x, 1000) for x in range(1000)])
    d1 = sorted([randint(x, 1000) for x in range(1000)])

    args = [a, a1, b, b1, c, c1, d, d1]

    print(main(args))
