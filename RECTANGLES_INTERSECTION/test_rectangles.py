import pytest

from RECTANGLES_INTERSECTION.rectangles import *


@pytest.fixture()
def fix_rect():
    return Rectangle(0, 0, 0, 0)


class TestMethods:
    @pytest.mark.parametrize('rect, expected', [
        ((7, 8, 1, 1), [[1, 1], [7, 8]]),
        ((11, 15, 4, 5), [[4, 5], [11, 15]]),
        ((0, 0, -1, -1), [[-1, -1], [0, 0]])
    ])
    def test_reverse_init(self, rect, expected):
        rect = Rectangle(*rect)
        assert rect.rect == expected

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(2, 3, 8, 7),
         Rectangle(1, 5, 13, 10))
    ]
                             )
    def test__and__(self, rect1, rect2):
        assert rect1.__and__(rect2)
        assert rect1 & rect2

    @pytest.mark.parametrize('rect, expected', [
        (Rectangle(2, 3, 8, 7), '[[2, 3], [8, 7]]'),
        (Rectangle(1, 5, 13, 10), '[[1, 5], [13, 10]]'),
        (Rectangle(13, 10, 1, 5), '[[1, 5], [13, 10]]'),
    ]
                             )
    def test__str__(self, rect, expected):
        assert rect.__str__() == expected

    @pytest.mark.parametrize('rect, expected', [
        (Rectangle(2, 3, 8, 7), '[[2, 3], [8, 7]]'),
        (Rectangle(1, 5, 13, 10), '[[1, 5], [13, 10]]'),
        (Rectangle(13, 10, 1, 5), '[[1, 5], [13, 10]]'),
    ]
                             )
    def test__repr__(self, rect, expected):
        assert rect.__repr__() == expected
        assert rect.__repr__() == rect.__str__()

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(2, 3, 8, 7),
         Rectangle(1, 5, 13, 10))
    ]
                             )
    def test_intersection(self, rect1, rect2):
        assert rect1.intersection(rect2)

    @pytest.mark.parametrize('params, expected', [
        ((1, 5, -1, -5), None),
        ((0, 0, 1, 1), None),
        ((0, 0, -1, -5), None),
        ((1, 5, 1, 5), [1, 5]),
        ((-3, -1, -5, -2), [-3, -2]),
        ((0, 0, 0, 0), [0, 0]),

    ])
    def test_xy_cross(self, fix_rect, params, expected):
        assert fix_rect.xy_cross(*params) == expected


class TestValues:
    @pytest.mark.parametrize('rect1, rect2, expected', [
        (Rectangle(2, 3, 8, 7), Rectangle(1, 5, 13, 10), 'Intersection'),
        (Rectangle(1, 1, 5, 5), Rectangle(1, 5, 5, 10), 'Intersection'),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 10, 10), 'Intersection'),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 4, 4), 'Intersection'),

        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 1, 1), 'Full overlapping'),
        (Rectangle(1, 4, 5, 8), Rectangle(5, 8, 1, 4), 'Full overlapping'),
        (Rectangle(1, 1, 5, 1), Rectangle(1, 1, 5, 1), 'Full overlapping'),

        (Rectangle(1, 1, 5, 5), Rectangle(-1, -1, -5, -5), 'No intersection'),
        (Rectangle(0, 0, 0, 0), Rectangle(1, 1, 1, 1), 'No intersection')
    ]
                             )
    def test_result_intersection(self, rect1, rect2, expected):
        message, new_rect = rect1 & rect2
        assert message == expected

    @pytest.mark.parametrize('rect1, rect2, expected', [
        (Rectangle(2, 3, 8, 7), Rectangle(1, 5, 13, 10), [[2, 5], [8, 7]]),
        (Rectangle(1, 1, 5, 5), Rectangle(1, 1, 5, 5), [[1, 1], [5, 5]]),
        (Rectangle(1, 1, 5, 5), Rectangle(5, 1, 10, 5), [[5, 1], [5, 5]]),
        (Rectangle(1, 1, 5, 5), Rectangle(2, 2, 6, 6), [[2, 2], [5, 5]]),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 3, 3), [[1, 1], [1, 1]]),
        (Rectangle(1, 1, 5, 1), Rectangle(1, 1, 5, 1), [[1, 1], [5, 1]]),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 10, 10), [[4, 4], [10, 10]]),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 6, 7), [[4, 4], [6, 7]])
    ]
                             )
    def test_result_correct_values(self, rect1, rect2, expected):
        message, new_rect = rect1 & rect2
        assert new_rect.rect == expected

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(2, 3, 8, 7), Rectangle(1, 5, 13, 10)),
        (Rectangle(1, 1, 5, 5), Rectangle(1, 1, 5, 5)),
        (Rectangle(1, 1, 5, 5), Rectangle(5, 1, 10, 5)),
        (Rectangle(1, 1, 5, 5), Rectangle(2, 2, 6, 6)),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 3, 3)),
        (Rectangle(1, 1, 5, 1), Rectangle(1, 1, 5, 1)),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 10, 10)),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 6, 7))
    ]
                             )
    def test_result_isinstance(self, rect1, rect2):
        message, new_rect = rect1 & rect2
        assert isinstance(new_rect, Rectangle)

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(1, 1, 5, 5), Rectangle(-1, -1, -5, -5)),
        (Rectangle(0, 0, 0, 0), Rectangle(1, 1, 1, 1))
    ]
                             )
    def test_result_none_values(self, rect1, rect2):
        message, new_rect = rect1 & rect2
        assert not new_rect


if __name__ == '__main__':
    pytest.main()
