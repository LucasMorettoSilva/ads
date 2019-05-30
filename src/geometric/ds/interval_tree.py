from functools                            import cmp_to_key
from statistics                           import median

from src.abc.decomposable.decomposable_sp import DecomposableSP

from src.geometric.prim.interval          import Interval


class IntervalTree(DecomposableSP):

    class __Node:

        def __init__(self, x_mid, i_mid):
            self.x_mid     = x_mid
            self.left_mid  = sorted(i_mid, key=cmp_to_key(Interval.min_order))
            self.right_mid = sorted(i_mid, key=cmp_to_key(Interval.max_order))

            # Children
            self.left  = None
            self.right = None

    def __init__(self, intervals):
        if intervals is None:
            raise ValueError("Invalid argument 'intervals' of None Type")

        self.__intervals = set(intervals)
        self.__root = self.__build(intervals)

    def __len__(self):
        return len(self.__intervals)

    def __build(self, intervals):
        if len(intervals) == 0:
            return None

        points = set()
        for i in intervals:
            points.add(i.min)
            points.add(i.max)

        x_mid  = median(points)

        i_mid   = self.__build_mid_intervals(x_mid, intervals)
        i_left  = self.__build_left_intervals(x_mid, intervals)
        i_right = self.__build_right_intervals(x_mid, intervals)

        v       = self.__Node(x_mid, i_mid)
        v.left  = self.__build(i_left)
        v.right = self.__build(i_right)

        return v

    def unbuild(self):
        return self.__intervals

    @staticmethod
    def __build_mid_intervals(x_mid, intervals):
        i_mid = list()
        for i in intervals:
            if x_mid in i:
                i_mid.append(i)
        return i_mid

    @staticmethod
    def __build_left_intervals(x_mid, intervals):
        i_left = list()
        for i in intervals:
            if x_mid > i.max:
                i_left.append(i)
        return i_left

    @staticmethod
    def __build_right_intervals(x_mid, intervals):
        i_right = list()
        for i in intervals:
            if x_mid < i.min:
                i_right.append(i)
        return i_right

    def query(self, point):
        if point is None:
            raise ValueError("Invalid argument 'point' of None Type")
        res = set()
        self.__query(self.__root, point, res)
        return res

    def __query(self, v, point, res):
        if v is None:
            return

        if point < v.x_mid:
            for i in v.left_mid:
                if point in i:
                    res.add(i)
                else:
                    break
            self.__query(v.left, point, res)
        else:
            for i in reversed(v.right_mid):
                if point in i:
                    res.add(i)
                else:
                    break
            self.__query(v.right, point, res)

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
