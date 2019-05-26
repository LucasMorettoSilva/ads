import random
import unittest

from src.geometric.ds.interval_tree import IntervalTree

from src.geometric.prim.interval    import Interval


class TestIntervalTree(unittest.TestCase):

    def test_constructor_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            IntervalTree(None)

    def test_constructor_withEmptySetOfIntervals_shouldCreateEmptyTree(self):
        tree = IntervalTree([])
        self.assertEqual(0, len(tree))

    def test_constructor_withCopiesOfOnlyOneInterval_shouldIgnoreCopiesAndConstructOneSizedTree(self):
        intervals = list()
        for _ in range(1000):
            intervals.append(Interval(1, 1))

        tree = IntervalTree(intervals)
        self.assertEqual(1, len(tree))

    def test_constructor_withCopiesOfOneFiveHundredIntervals_shouldIgnoreCopiesAndConstructFiveHundredSizedTree(self):
        intervals = list()
        for i in range(500):
            for _ in range(10):
                intervals.append(Interval(i, i))

        tree = IntervalTree(intervals)
        self.assertEqual(500, len(tree))

    def test_constructor_withNotEqualIntervals_shouldCreateTreeWithAllGivenIntervals(self):
        intervals = list()
        for i in range(1000):
            intervals.append(Interval(i, i))

        tree = IntervalTree(intervals)
        self.assertEqual(1000, len(tree))

    def test_query_withNoneTypeArgument_shouldRaiseValueError(self):
        intervals = list()
        for i in range(10):
            intervals.append(Interval(i, i))
        tree = IntervalTree(intervals)

        with self.assertRaises(ValueError):
            tree.query(None)

    def test_query_withEmptyTree_shouldReturnEmptySet(self):
        tree = IntervalTree([])
        for i in range(1000):
            a = random.uniform(0, i)
            self.assertEqual(set(), tree.query(a))

    def test_query_withPointNotInAnyInterval_shouldReturnEmptySet(self):
        leftmost  = None
        rightmost = None
        intervals = list()
        for i in range(1000):
            a = Interval(random.uniform(0, i), random.uniform(i, 1000))
            if leftmost is None or a.min < leftmost:
                leftmost = a.min
            if rightmost is None or a.max > rightmost:
                rightmost = a.max
            intervals.append(a)

        tree = IntervalTree(intervals)
        self.assertEqual(set(), tree.query(leftmost  - 1))
        self.assertEqual(set(), tree.query(rightmost + 1))

    def test_query_withPointInSomeIntervals_shouldReturnSetWithIntervalsThatContainQueryPoint(self):
        point     = random.uniform(0, 1000)
        expected  = set()
        intervals = list()
        for i in range(1000):
            a = Interval(i, 1000)
            b = Interval(random.uniform(0, 1000), random.uniform(0, 1000))
            if point in a:
                expected.add(a)
            if point in b:
                expected.add(b)
            intervals.append(a)
            intervals.append(b)

        tree = IntervalTree(intervals)
        self.assertEqual(expected, tree.query(point))
