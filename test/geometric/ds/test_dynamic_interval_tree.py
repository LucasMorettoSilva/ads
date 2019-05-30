import random
import unittest

from src.abc.decomposable.dynamic_deletion  import DynamicDeletion
from src.abc.decomposable.dynamic_insertion import DynamicInsertion

from src.geometric.ds.interval_tree         import IntervalTree

from src.geometric.prim.interval            import Interval


class TestDynamicIntervalTree(unittest.TestCase):

    def test_constructor_withDynamicInsertionInterface_shouldCreateEmptyTree(self):
        tree = DynamicInsertion(IntervalTree)
        self.assertEqual(0, len(tree))

    def test_insert_withNoneTypeArgumentAndDynamicInsertionInterface_shouldRaiseValueError(self):
        tree = DynamicInsertion(IntervalTree)
        with self.assertRaises(ValueError):
            tree.insert(None)

    def test_insert_withValidArgumentAndDynamicInsertionInterface_shouldInsertIntervalIntoTree(self):
        expected = set()
        tree = DynamicInsertion(IntervalTree)
        for i in range(1, 1000):
            tree.insert(Interval(i, i))
            expected.add(Interval(i, i))
            self.assertEqual(i, len(tree))
        self.assertEqual(expected, tree.all())

    def test_query_withNoneTypeArgumentAndDynamicInsertionInterface_shouldRaiseValueError(self):
        tree = DynamicInsertion(IntervalTree)
        with self.assertRaises(ValueError):
            tree.query(None)

    def test_query_withEmptyTreeAndDynamicInsertionInterface_shouldReturnEmptySet(self):
        tree = DynamicInsertion(IntervalTree)
        for _ in range(1000):
            a = random.uniform(0, 1000)
            self.assertEqual(set(), tree.query(a))

    def test_query_withPointNotInAnyIntervalAndDynamicInsertionInterface_shouldReturnEmptySet(self):
        leftmost  = None
        rightmost = None
        tree = DynamicInsertion(IntervalTree)
        for i in range(500):
            a = Interval(random.uniform(0, i), random.uniform(i, 1000))
            if leftmost is None or a.min < leftmost:
                leftmost = a.min
            if rightmost is None or a.max > rightmost:
                rightmost = a.max
            tree.insert(a)
            self.assertEqual(set(), tree.query(leftmost - 1))
            self.assertEqual(set(), tree.query(rightmost + 1))

    def test_query_withPointInSomeIntervalsAndDynamicInsertionInterface_shouldReturnSetWithIntervalsThatContainQueryPoint(self):
        tree  = DynamicInsertion(IntervalTree)
        point = random.uniform(0, 1000)
        expected = set()
        for i in range(500):
            a = Interval(i, 1000)
            b = Interval(random.uniform(0, 1000), random.uniform(0, 1000))
            if point in a:
                expected.add(a)
            if point in b:
                expected.add(b)
            tree.insert(a)
            tree.insert(b)
            self.assertEqual(expected, tree.query(point))

    def test_constructor_withDynamicDeletionInterfaceAndEmptyData_shouldCreateEmptyTree(self):
        tree = DynamicDeletion(IntervalTree, [])
        self.assertEqual(0, len(tree))

    def test_constructor_withDynamicDeletionInterfaceAndNoneTypeArgumentData_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            DynamicDeletion(IntervalTree, None)

    def test_constructor_withDynamicDeletionInterfaceAndDuplicatedIntervalsInData_shouldRemoveDuplicatesAndCreateTree(self):
        intervals = list()
        for i in range(500):
            for _ in range(10):
                intervals.append(Interval(i, i))

        tree = DynamicDeletion(IntervalTree, intervals)
        self.assertEqual(500, len(tree))
        self.assertEqual(set(intervals), tree.all())

    def test_delete_withNoneTypeArgumentAndDynamicDeletionInterface_shouldRaiseValueError(self):
        tree = DynamicDeletion(IntervalTree, [])
        with self.assertRaises(ValueError):
            tree.delete(None)

    def test_delete_withIntervalInTreeAndDynamicDeletionInterface_shouldDeleteIntervalFromTree(self):
        intervals = set()
        for i in range(1, 500):
            intervals.add(Interval(i, i))
        tree = DynamicDeletion(IntervalTree, intervals)

        for i in range(1, 500):
            tree.delete(Interval(i, i))
            intervals.remove(Interval(i, i))
            self.assertEqual(499 - i, len(tree))
            self.assertEqual(intervals, tree.all())

    def test_delete_withIntervalNotInTreeAndDynamicDeletionInterface_shouldNotAlterTree(self):
        intervals = set()
        for i in range(500):
            intervals.add(Interval(i, i))
        tree = DynamicDeletion(IntervalTree, intervals)

        for i in range(500, 1000):
            tree.delete(Interval(i, i))
            self.assertEqual(500, len(tree))
            self.assertEqual(intervals, tree.all())

    def test_query_withNoneTypeArgumentAndDynamicDeletionInterface_shouldRaiseValueError(self):
        tree = DynamicDeletion(IntervalTree, [])
        with self.assertRaises(ValueError):
            tree.query(None)

    def test_query_withEmptyTreeAndDynamicDeletionInterface_shouldReturnEmptySet(self):
        tree = DynamicDeletion(IntervalTree, [])
        for _ in range(1000):
            a = random.uniform(0, 1000)
            self.assertEqual(set(), tree.query(a))

    def test_query_withPointInSomeIntervalsAndDynamicDeletionInterface_shouldReturnSetWithIntervalsThatContainQueryPoint(self):
        intervals = set()
        expected  = set()
        point     = random.uniform(0, 1000)

        for i in range(500):
            a = Interval(i, 1000)
            b = Interval(random.uniform(0, 1000), random.uniform(0, 1000))
            if point in a:
                expected.add(a)
            if point in b:
                expected.add(b)
            intervals.add(a)
            intervals.add(b)

        tree = DynamicDeletion(IntervalTree, intervals)

        self.assertEqual(expected, tree.query(point))

        while len(expected) > 0:
            x = expected.pop()
            tree.delete(x)
            self.assertEqual(expected, tree.query(point))
