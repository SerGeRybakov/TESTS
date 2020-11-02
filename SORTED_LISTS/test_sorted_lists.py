from random import randint, choice

import pytest

from SORTED_LISTS import sorted_lists


@pytest.fixture()
def args():
    string1 = sorted([x for x in 'abcdefghijklmnopqrstuvwxyz' for _ in range(100)])
    string2 = sorted([x for x in 'abcdefghijklmnopqrstuvwxyz'.upper() for _ in range(100)])
    string3 = sorted([x for x in 'абвгдежзиклмнопрстуфхцчшщъыьэюя' for _ in range(100)])
    string4 = sorted([x for x in 'абвгдежзиклмнопрстуфхцчшщъыьэюя'.upper() for _ in range(100)])
    string5 = ['a']

    strings = [string1, string2, string3, string4, string5]

    a = sorted([randint(x, 100) for x in range(100)])
    a1 = sorted([randint(x, 100) for x in range(100)])
    b = sorted([randint(x, 500) for x in range(500)])
    b1 = sorted([randint(x, 500) for x in range(500)])
    c = sorted([randint(x, 1000) for x in range(1000)])
    c1 = sorted([randint(x, 1000) for x in range(1000)])
    d = sorted([randint(x, 10000) for x in range(10000)])
    d1 = sorted([randint(x, 10000) for x in range(10000)])
    e = [0, 0, 0, 0]
    nums = [a, a1, b, b1, c, c1, d, d1, e]

    return choice((strings, nums))


@pytest.fixture()
def min_element(min_list):
    return min(min_list)


@pytest.fixture()
def min_list(args):
    return min(args)


def test_main(args, min_element):
    result = sorted_lists.main(args)
    assert min_element == result[0]
    for i in range(len(result) + 1):
        try:
            assert result[i] <= result[i + 1]
        except IndexError:
            pass


def test_get_min_element(args, min_element):
    assert min_element == sorted_lists.get_min_element(args)


def test_create_new_sorted_list(args, min_element, min_list):
    new_lst, new_args = sorted_lists.create_new_sorted_list(args, min_element)
    assert new_lst == min_list
    assert min_list not in new_args


# def test_insert_in_place():
#     pass

# def test_sort_elements():
#     pass

if __name__ == '__main__':
    pytest.main()
