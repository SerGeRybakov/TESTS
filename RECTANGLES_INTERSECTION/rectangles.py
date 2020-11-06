class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.reverse_init()
        self.rect = [[self.x1, self.y1], [self.x2, self.y2]]

    def __str__(self):
        return f'[[{self.x1}, {self.y1}], [{self.x2}, {self.y2}]]'

    def __repr__(self):
        return self.__str__()

    def __and__(self, other):
        return self.intersection(other)

    def reverse_init(self):
        if not self.x1 <= self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if not self.y1 <= self.y2:
            self.y1, self.y2 = self.y2, self.y1

    @staticmethod
    def xy_cross(self1, self2, other1, other2):
        if self2 < other1 or other2 < self1:
            return
        return sorted([self1, self2, other1, other2])[1:-1]

    def intersection(self, other):
        if self.rect == other.rect:
            return f'Full overlapping', self

        xs = self.xy_cross(self.x1, self.x2, other.x1, other.x2)
        ys = self.xy_cross(self.y1, self.y2, other.y1, other.y2)

        if xs and ys:
            new_rect = Rectangle(xs[0], ys[0], xs[1], ys[1])
            return 'Intersection', new_rect

        return 'No intersection', None
