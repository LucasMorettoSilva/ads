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

