from src.geometric.prim.interval import Interval
from src.geometric.prim.point_2d import Point2D


class Segment:

    def __init__(self, p1, p2):
        if p1 is None:
            raise ValueError("Invalid argument 'p1' of None Type")
        if p2 is None:
            raise ValueError("Invalid argument 'p2' of None Type")

        if Point2D.yx_order(p1, p2) < 0:
            self.__upper = p1
            self.__lower = p2
        else:
            self.__upper = p2
            self.__lower = p1

    def __str__(self):
        return "[{}, {}]".format(self.__lower, self.__upper)

    def __repr__(self):
        return "[{}, {}]".format(self.__lower, self.__upper)

    def __hash__(self):
        return hash(self.__upper) ^ hash(self.__lower)

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, Segment):
            return self.__upper == other.__upper and \
                   self.__lower == other.__lower
        return False

    def __contains__(self, point):
        if not Point2D.collinear(point, self.__upper, self.__lower):
            return False

        if self.__upper.x != self.__lower.x:
            return self.__lower.x <= point.x <= self.__upper.x or \
                   self.__upper.x <= point.x <= self.__lower.x

        return self.__lower.y <= point.y <= self.__upper.y or \
               self.__upper.y <= point.y <= self.__lower.y

    @property
    def endpoints(self):
        return self.__lower, self.__upper

    @property
    def lower(self):
        return self.__lower

    @property
    def upper(self):
        return self.__upper

    @property
    def x_interval(self):
        return Interval(self.lower.x, self.upper.x)

    @property
    def y_interval(self):
        return Interval(self.lower.y, self.upper.y)
