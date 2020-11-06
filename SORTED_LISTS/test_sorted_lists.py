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
    b = sorted([randint(400, 500) for _ in range(500)])
    b1 = sorted([randint(400, 500) for _ in range(500)])
    c = sorted([randint(800, 1000) for _ in range(1000)])
    c1 = sorted([randint(800, 1000) for _ in range(1000)])
    d = sorted([randint(5000, 10000) for _ in range(10000)])
    d1 = sorted([randint(5000, 10000) for _ in range(10000)])
    e = [0, 0, 0, 0]
    nums = [d, d1, b, b1, a, a1, c, c1, e]

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


@pytest.mark.parametrize('new_list, new_element, expected_result', [
    (["a", "a", "a", "c", "c", "c"], "b", ["a", "a", "a", "b", "c", "c", "c"]),
    ([100, 200, 300, 500], 400, [100, 200, 300, 400, 500]),
    ([1.001, 1.002, 1.003, 1.005], 1, [1, 1.001, 1.002, 1.003, 1.005]),
])
def test_insert_in_place(new_list, new_element, expected_result):
    result = sorted_lists.insert_in_place(new_list, new_element)
    assert result == expected_result


@pytest.mark.parametrize('new_list, next_list, expected_result', [
    (["a", "a", "a", "c", "c", "c"], ["d", "e", "f"], ["a", "a", "a", "c", "c", "c", "d", "e", "f"]),
    ([100, 200, 300, 500], [501, 505, 507, 508], [100, 200, 300, 500, 501, 505, 507, 508]),
    ([5.001, 6.002, 8.003, 15.005], [10, 11.002, 12.003], [5.001, 6.002, 8.003, 10, 11.002, 12.003, 15.005]),
])
def test_sort_elements1(new_list, next_list, expected_result):
    result = sorted_lists.sort_elements(new_list, next_list)
    assert result == expected_result


@pytest.mark.parametrize('new_list, next_list, expected_result', [
    (["a", "a", "a", "c", "c", "c"], ["a", "c"], ["a", "a", "a", "a", "c", "c", "c", "c"]),
    ([100, 200, 300, 500], [100, 200], [100, 100, 200, 200, 300, 500]),
    ([1.1, 1.2, 1.3, 1.5], [1.2, 1.5], [1.1, 1.2, 1.2, 1.3, 1.5, 1.5]),
])
def test_sort_elements2(new_list, next_list, expected_result):
    result = sorted_lists.sort_elements(new_list, next_list)
    assert result == expected_result


if __name__ == '__main__':
    pytest.main()
