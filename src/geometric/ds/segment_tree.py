from src.abc.static import Static

from src.geometric.prim.interval import Interval


class SegmentTree(Static):

    class __Node:

        def __init__(self, b, e):
            self.b = b
            self.e = e
            self.i = Interval(b, e)
            self.left  = None
            self.right = None
            self.aux = set()

    def __init__(self, intervals):
        if intervals is None:
            raise ValueError("Invalid argument 'intervals' of None Type")

        self.__intervals = set(intervals)
        if len(self.__intervals) == 0:
            self.__root = None

        else:
            endpoints = set()
            endpoints.add(float("-inf"))
            endpoints.add(float("inf"))
            for i in self.__intervals:
                endpoints.add(i.min)
                endpoints.add(i.max)

            self.__root = self.__build(sorted(endpoints))
            for i in intervals:
                self.__put_interval(self.__root, i)

    def __len__(self):
        return len(self.__intervals)

    def __build(self, points, a=None, b=None):
        if len(points) == 0:
            return None
        if len(points) == 1 or len(points) == 2:
            return self.__Node(a, b)

        m = len(points) // 2
        if a is None:
            a = points[0]
            b = points[-1]
        v = self.__Node(a, b)
        v.left  = self.__build(points[:m], points[0], points[m])
        v.right = self.__build(points[m:], points[m], points[-1])
        return v

    def __put_interval(self, v, interval):
        if v.b in interval and v.e in interval:
            v.aux.add(interval)
            return
        if v.left and v.left.i.intersects(interval):
            self.__put_interval(v.left, interval)
        if v.right and v.right.i.intersects(interval):
            self.__put_interval(v.right, interval)

    def query(self, point):
        if point is None:
            raise ValueError("Invalid argument 'point' of None Type")
        res = set()
        self.__query(self.__root, point, res)
        return res

    def __query(self, v, point, res):
        if v is None:
            return
        if point in v.i:
            res.update(v.aux)
        if v.left and point in v.left.i:
            self.__query(v.left, point, res)
        else:
            self.__query(v.right, point, res)

    def unbuild(self):
        return self.__intervals
