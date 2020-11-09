import pytest

from RECTANGLES_INTERSECTION.rectangles import Rectangle


@pytest.fixture()
def fixed_rect():
    return Rectangle(11, 15, 4, 5)


class TestMethods:

    def test__slots__(self, fixed_rect):
        with pytest.raises(AttributeError):
            fixed_rect.x3 = 0

    def test__rect_property_getter(self, fixed_rect):
        assert fixed_rect._rect == [[4, 5], [11, 15]]
        fixed_rect.x1, fixed_rect.y1 = 0, 0
        assert fixed_rect._rect == [[0, 0], [11, 15]]

    def test__rect_property_setter(self, fixed_rect):
        with pytest.raises(AttributeError):
            fixed_rect._rect = 0

    def test__rect_property_deleter(self, fixed_rect):
        with pytest.raises(AttributeError):
            del fixed_rect._rect

    @pytest.mark.parametrize('rect, expected', [
        (Rectangle(7, 8, 1, 1), [[1, 1], [7, 8]]),
        (Rectangle(11, 15, 4, 5), [[4, 5], [11, 15]]),
        (Rectangle(0, 0, -1, -1), [[-1, -1], [0, 0]])
    ])
    def test_reverse_init(self, rect, expected):
        assert rect._rect == expected

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(2, 3, 8, 7),
         Rectangle(1, 5, 13, 10))
    ])
    def test__and__(self, rect1, rect2):
        assert rect1 & rect2

    @pytest.mark.parametrize('rect, expected', [
        (Rectangle(2, 3, 8, 7), '[[2, 3], [8, 7]]'),
        (Rectangle(1, 5, 13, 10), '[[1, 5], [13, 10]]'),
        (Rectangle(13, 10, 1, 5), '[[1, 5], [13, 10]]'),
    ])
    def test__str__(self, rect, expected):
        assert str(rect) == expected

    @pytest.mark.parametrize('rect, expected', [
        (Rectangle(2, 3, 8, 7), 'Rectangle(2, 3, 8, 7)'),
        (Rectangle(1, 5, 13, 10), 'Rectangle(1, 5, 13, 10)'),
        (Rectangle(13, 10, 1, 5), 'Rectangle(1, 5, 13, 10)'),
    ])
    def test__repr__(self, rect, expected):
        assert repr(rect) == expected

    @pytest.mark.parametrize('rect1, rect2, expected', [
        (Rectangle(2, 3, 8, 7), Rectangle(1, 5, 13, 10), False),
        (Rectangle(1, 1, 5, 5), Rectangle(1, 5, 5, 6), False),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 10, 10), False),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 4, 4), False),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 5, 1), False),
        (Rectangle(1, 1, 5, 5), Rectangle(-1, -1, -5, -5), False),
        (Rectangle(0, 0, 0, 0), Rectangle(1, 1, 1, 1), False),

        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 1, 1), True),
        (Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4), True),
        (Rectangle(1, 4, 5, 8), Rectangle(5, 8, 1, 4), True),
        (Rectangle(1, 1, 5, 1), Rectangle(1, 1, 5, 1), True),
    ])
    def test__eq__(self, rect1, rect2, expected):
        result = rect1 == rect2
        assert result == expected

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(2, 3, 8, 7),
         Rectangle(1, 5, 13, 10))
    ])
    def test_intersection(self, rect1, rect2):
        assert rect1.intersection(rect2)


class TestValues:
    @pytest.mark.parametrize('params', [
        (5, 1, -5, -1),
        (1, 5, -1, -5),
        (5, 1, -5, -1),
    ])
    def test_xy_cross_value_error(self, params: tuple):
        with pytest.raises(ValueError, match=r'Wrong section values passed'):
            Rectangle._xy_cross(*params)

    @pytest.mark.parametrize('params, expected', [
        ((1, 1, 0, 0), None),
        ((0, 0, 1, 1), None),
        ((0, 0, -5, -1), None),
        ((1, 5, 1, 5), [1, 5]),
        ((-3, -1, -5, -2), [-3, -2]),
        ((0, 0, 0, 0), [0, 0]),
        ((0, 3, 0, 3), [0, 3]),

    ])
    def test_xy_cross(self, params, expected):
        assert Rectangle._xy_cross(*params) == expected

    @pytest.mark.parametrize('rect1, rect2, expected', [
        (Rectangle(2, 3, 8, 7), Rectangle(1, 5, 13, 10), 'Intersection'),
        (Rectangle(1, 1, 5, 5), Rectangle(1, 5, 5, 10), 'Intersection'),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 10, 10), 'Intersection'),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 4, 4), 'Intersection'),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 5, 1), 'Intersection'),

        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 1, 1), 'Full overlapping'),
        (Rectangle(1, 4, 5, 8), Rectangle(5, 8, 1, 4), 'Full overlapping'),
        (Rectangle(1, 1, 5, 1), Rectangle(1, 1, 5, 1), 'Full overlapping'),

        (Rectangle(1, 1, 5, 5), Rectangle(-1, -1, -5, -5), 'No intersection'),
        (Rectangle(0, 0, 0, 0), Rectangle(1, 1, 1, 1), 'No intersection')
    ])
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
    ])
    def test_result_correct_values(self, rect1, rect2, expected):
        message, new_rect = rect1 & rect2
        assert new_rect._rect == expected

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(2, 3, 8, 7), Rectangle(1, 5, 13, 10)),
        (Rectangle(1, 1, 5, 5), Rectangle(1, 1, 5, 5)),
        (Rectangle(1, 1, 5, 5), Rectangle(5, 1, 10, 5)),
        (Rectangle(1, 1, 5, 5), Rectangle(2, 2, 6, 6)),
        (Rectangle(1, 1, 1, 1), Rectangle(1, 1, 3, 3)),
        (Rectangle(1, 1, 5, 1), Rectangle(1, 1, 5, 1)),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 10, 10)),
        (Rectangle(1, 1, 10, 10), Rectangle(4, 4, 6, 7))
    ])
    def test_result_isinstance(self, rect1, rect2):
        message, new_rect = rect1 & rect2
        assert isinstance(new_rect, Rectangle)

    @pytest.mark.parametrize('rect1, rect2', [
        (Rectangle(1, 1, 5, 5), Rectangle(-1, -1, -5, -5)),
        (Rectangle(0, 0, 0, 0), Rectangle(1, 1, 1, 1))
    ])
    def test_result_none_values(self, rect1, rect2):
        message, new_rect = rect1 & rect2
        assert not new_rect


if __name__ == '__main__':
    pytest.main()
