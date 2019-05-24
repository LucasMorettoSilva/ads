import abc
import math


class Point(abc.ABC):

    def __init__(self, coords):
        if coords is None:
            raise ValueError("Invalid argument 'coords' of None Type")
        if len(coords) == 0:
            raise ValueError("Point must have at least one coordinate")
        for c in coords:
            if c is None:
                raise ValueError("Invalid coordinate of None Type")
            if math.isinf(c):
                raise ValueError("Coordinates must be finite")
            if math.isnan(c):
                raise ValueError("Coordinates cannot be NaN")
        self._coords = coords

    def __str__(self):
        res = "({},".format(self._coords[0])
        for i in range(1, len(self._coords)):
            res += " {},".format(self._coords[i])
        return res[:-1] + ")"

    def __eq__(self, other):
        if other is self:
            return True
        if isinstance(other, Point):
            return self._coords == other._coords
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        hash_code = 1
        for c in self._coords:
            hash_code = 31 * hash_code + hash(c)
        return hash_code

    def __getitem__(self, item):
        if item <= 0 or item > len(self._coords):
            raise ValueError("Invalid dimension = {}".format(item))
        return self._coords[item - 1]

    @property
    def coordinates(self):
        return self._coords

    @property
    def dimension(self):
        return len(self._coords)
