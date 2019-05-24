import math

from src.abc.point import Point


class Point2D(Point):

    def __init__(self, x, y):
        if x is None:
            raise ValueError("Invalid argument 'x' of None Type")
        if y is None:
            raise ValueError("Invalid argument 'y' of None Type")
        super().__init__([x, y])

    @property
    def x(self):
        return self._coords[0]

    @property
    def y(self):
        return self._coords[1]

    @property
    def r(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def theta(self):
        return math.atan2(self.y, self.x)

    def angle_to(self, point):
        if point is None:
            raise ValueError("Invalid argument 'point' of None Type")
        return math.atan2(point.y - self.y, point.x - self.x)

    def distance_to(self, point):
        if point is None:
            raise ValueError("Invalid argument 'point' of None Type")
        return math.sqrt(self.distance_squared_to(point))

    def distance_squared_to(self, point):
        if point is None:
            raise ValueError("Invalid argument 'point' of None Type")
        dx = self.x - point.x
        dy = self.y - point.y
        return dx ** 2 + dy ** 2

    @staticmethod
    def area2(a, b, c):
        if a is None or \
           b is None or \
           c is None:
            raise ValueError("Invalid argument of None Type")
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

    @staticmethod
    def area_sign(a, b, c):
        if a is None or \
           b is None or \
           c is None:
            raise ValueError("Invalid argument of None Type")
        area2 = Point2D.area2(a, b, c)
        if area2 > 0:
            return 1
        if area2 < 0:
            return -1
        return 0

    @staticmethod
    def ccw(a, b, c):
        if a is None or \
           b is None or \
           c is None:
            raise ValueError("Invalid argument of None Type")
        return Point2D.area_sign(a, b, c)

    @classmethod
    def x_order(cls, a, b):
        if a.x < b.x:
            return -1
        if a.x > b.x:
            return 1
        return 0

    @classmethod
    def y_order(cls, a, b):
        if a.y < b.y:
            return -1
        if a.y > b.y:
            return 1
        return 0

    @classmethod
    def xy_order(cls, a, b):
        cmp_x = cls.x_order(a, b)
        if cmp_x == 0:
            return cls.y_order(a, b)
        return cmp_x

    @classmethod
    def yx_order(cls, a, b):
        cmp_y = cls.y_order(a, b)
        if cmp_y == 0:
            return cls.x_order(a, b)
        return cmp_y
