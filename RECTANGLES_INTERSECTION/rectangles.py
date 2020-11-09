class Rectangle:
    __slots__ = ("x1", "y1", "x2", "y2")

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.reverse_init()

    @property
    def _rect(self):
        return [[self.x1, self.y1], [self.x2, self.y2]]

    def __str__(self):
        return f"{self._rect}"

    def __repr__(self):
        return f"{type(self).__name__}({self.x1!r}, {self.y1!r}, {self.x2!r}, {self.y2!r})"

    def __and__(self, other):
        return self.intersection(other)

    def __eq__(self, other):
        return self._rect == other._rect

    def reverse_init(self):
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

    @staticmethod
    def _xy_cross(self1, self2, other1, other2):
        if self1 > self2 or other1 > other2:
            raise ValueError(f"Wrong section values passed")

        if self2 < other1 or other2 < self1:
            return
        return sorted([self1, self2, other1, other2])[1:-1]

    def intersection(self, other):
        if self == other:
            return f"Full overlapping", self

        xs = self._xy_cross(self.x1, self.x2, other.x1, other.x2)
        ys = self._xy_cross(self.y1, self.y2, other.y1, other.y2)

        if xs and ys:
            new_rect = Rectangle(xs[0], ys[0], xs[1], ys[1])
            return "Intersection", new_rect

        return "No intersection", None
