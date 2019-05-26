class Interval:

    def __init__(self, a, b, cmp=None):
        self.__cmp = cmp
        if self.__compare(a, b) < 0:
            self.__min = a
            self.__max = b
        else:
            self.__min = b
            self.__max = a

    def __hash__(self):
        return 31 * hash(self.__min) + hash(self.__max)

    def __str__(self):
        return "[{}, {}]".format(self.__min, self.__max)

    def __repr__(self):
        return "[{}, {}]".format(self.__min, self.__max)

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, Interval):
            return \
                self.__compare(self.min, other.min) == 0 and \
                self.__compare(self.max, other.max) == 0
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def contains(self, x):
        return not self.__less(self.__max, x) and \
               not self.__less(x, self.__min)

    def __contains__(self, item):
        return self.contains(item)

    def intersects(self, a):
        if self.__less(self.__max, a.min):
            return False
        if self.__less(a.max, self.__min):
            return False
        return True

    def endpoints(self):
        return self.__min, self.__max

    @classmethod
    def min_order(cls, a, b):
        if a.min < b.min:
            return -1
        if a.min > b.min:
            return 1
        if a.max < b.max:
            return -1
        if a.max > b.max:
            return 1
        return 0

    @classmethod
    def max_order(cls, a, b):
        if a.max < b.max:
            return -1
        if a.max > b.max:
            return 1
        if a.min < b.min:
            return -1
        if a.min > b.min:
            return 1
        return 0

    @classmethod
    def length_order(cls, a, b):
        if a.length < b.length:
            return -1
        if a.length > b.length:
            return 1
        return 0

    @property
    def max(self):
        return self.__max

    @property
    def min(self):
        return self.__min

    @property
    def length(self):
        return self.__max - self.__min

    def __compare(self, a, b):
        if self.__cmp:
            return self.__cmp(a, b)
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

    def __less(self, a, b):
        return self.__compare(a, b) < 0
