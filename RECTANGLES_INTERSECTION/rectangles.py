class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.reverse_init()
        self.rect = [[self.x1, self.y1], [self.x2, self.y2]]

    def __str__(self):
        return f'[[{self.x1}, {self.y1}],[{self.x2}, {self.y2}]]'

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
            return f'Full overlapping at {self}'

        xs = self.xy_cross(self.x1, self.x2, other.x1, other.x2)
        ys = self.xy_cross(self.y1, self.y2, other.y1, other.y2)

        if xs and ys:
            new_rect = Rectangle(xs[0], ys[0], xs[1], ys[1])
            if (xs == [self.x1, self.x2] and ys == [self.y1, self.y2]) or \
                    (xs == [other.x1, other.x2] and ys == [other.y1, other.y2]):
                return f'Overlapping at {new_rect}'

            return f'Intersection at {new_rect}'

        return f'No intersection'


# Intersection [(2, 5), (8, 7)]
r1 = Rectangle(2, 3, 8, 7)
r2 = Rectangle(1, 5, 13, 10)
print(r1 & r2)
print()

# Full overlapping
r3 = Rectangle(1, 1, 5, 5)
r4 = Rectangle(1, 1, 5, 5)
print(r3 & r4)
print()

# No intersection
r5 = Rectangle(1, 1, 5, 5)
r6 = Rectangle(-1, -1, -5, -5)
print(r5 & r6)
print()

# Intersection at x-line [(1,5),(5,5)]
r7 = Rectangle(1, 1, 5, 5)
r8 = Rectangle(1, 5, 5, 10)
print(r7 & r8)
print()

# Intersection at y-line[(5,5),(1,5)]
r7 = Rectangle(1, 1, 5, 5)
r8 = Rectangle(5, 1, 10, 5)
print(r7 & r8)
print()

# Equal square. Intersection at [(2,2),(5,5)]
r9 = Rectangle(1, 1, 5, 5)
r10 = Rectangle(2, 2, 6, 6)
print(r9 & r10)
print()

# Full overlapping point
r11 = Rectangle(1, 1, 1, 1)
r12 = Rectangle(1, 1, 1, 1)
print(r11 & r12)
print()

# Overlapping point at [[1, 1],[1, 1]]
r13 = Rectangle(1, 1, 1, 1)
r14 = Rectangle(1, 1, 3, 3)
print(r13 & r14)
print()

# Full overlapping lines at x-line [[1, 1],[5, 1]]
r15 = Rectangle(1, 1, 5, 1)
r16 = Rectangle(1, 1, 5, 1)
print(r15 & r16)
print()

# Full overlapping lines at y-line [[1, 1],[1, 5]]
r17 = Rectangle(1, 1, 1, 5)
r18 = Rectangle(1, 1, 1, 5)
print(r17 & r18)
print()

# One inside another 1. Overlapping at [[4, 4],[10, 10]]
r19 = Rectangle(1, 1, 10, 10)
r20 = Rectangle(4, 4, 10, 10)
print(r19 & r20)
print()

# One inside another 2. Overlapping at [[4, 4],[6, 7]]
r21 = Rectangle(1, 1, 10, 10)
r22 = Rectangle(4, 4, 6, 7)
print(r21 & r22)
print()

# Reversed init. Intersection at [[4, 5],[7, 8]]
r23 = Rectangle(7, 8, 1, 1)
r24 = Rectangle(11, 15, 4, 5)
print(r23 & r24)
print()
