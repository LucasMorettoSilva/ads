from src.abc.decomposable.decomposable_sp import DecomposableSP

from src.geometric.prim.interval          import Interval


class SegmentTree(DecomposableSP):

    class __Node:

        def __init__(self, i):
            self.i     = i
            self.left  = None
            self.right = None
            self.segments = set()

    def __init__(self, segments):
        if segments is None:
            raise ValueError("Invalid argument 'segments' of None Type")

        self.__segments = set(segments)

        if   len(self.__segments) == 0:
            self.__root = None
        elif len(self.__segments) == 1:
            i = self.__segments.pop()
            self.__root = self.__Node(i)
            self.__segments.add(i)
        else:
            endpoints = set()
            for i in self.__segments:
                endpoints.add(i.min)
                endpoints.add(i.max)

            self.__root = self.__build(sorted(endpoints), 0, len(endpoints) - 1)

        for i in segments:
            self.__put_interval(self.__root, i)

    def __len__(self):
        return len(self.__segments)

    def __build(self, points, a, b):
        if a + 1 == b:
            v = self.__Node(Interval(points[a], points[b]))
            return v

        m = (a + b) // 2

        v       = self.__Node(Interval(points[a], points[b]))
        v.left  = self.__build(points, a, m)
        v.right = self.__build(points, m, b)
        return v

    def __put_interval(self, v, interval):
        if v.i.min in interval and v.i.max in interval:
            v.segments.add(interval)
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
        if v is None or (point < v.i.min or point > v.i.max):
            return
        if point in v.i:
            res.update(v.segments)
        if v.left and point in v.left.i:
            self.__query(v.left, point, res)
        else:
            self.__query(v.right, point, res)

    def unbuild(self):
        return self.__segments

    @classmethod
    def operator(cls, a, b):
        if a is None or b is None:
            raise ValueError("Invalid argument of None Type")
        a.update(b)
        return a

    @classmethod
    def operator_inverse(cls, a, b):
        if a is None or b is None:
            raise ValueError("Invalid argument of None Type")
        a.difference_update(b)
        return a
