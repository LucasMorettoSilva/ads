import random
import unittest

from src.geometric.ds.dynamic_interval_tree import DynamicIntervalTree

from src.geometric.prim.interval            import Interval


class TestDynamicIntervalTree(unittest.TestCase):

    def test_constructor_shouldCreateEmptyTree(self):
        tree = DynamicIntervalTree()
        self.assertEqual(0, len(tree))

    def test_insert_withNoneTypeArgument_shouldRaiseValueError(self):
        tree = DynamicIntervalTree()
        with self.assertRaises(ValueError):
            tree.insert(None)

    def test_insert_withValidArgument_shouldInsertIntervalIntoTree(self):
        expected = set()
        tree = DynamicIntervalTree()
        for i in range(1, 1000):
            tree.insert(Interval(i, i))
            expected.add(Interval(i, i))
            self.assertEqual(i, len(tree))
        self.assertEqual(expected, tree.all())

    def test_query_withNoneTypeArgument_shouldRaiseValueError(self):
        tree = DynamicIntervalTree()
        with self.assertRaises(ValueError):
            tree.query(None)

    def test_query_withEmptyTree_shouldReturnEmptySet(self):
        tree = DynamicIntervalTree()
        for _ in range(1000):
            a = Interval(random.uniform(0, 1000), random.uniform(0, 1000))
            self.assertEqual(set(), tree.query(a))

    def test_query_withPointNotInAnyInterval_shouldReturnEmptySet(self):
        leftmost  = None
        rightmost = None
        tree = DynamicIntervalTree()
        for i in range(500):
            a = Interval(random.uniform(0, i), random.uniform(i, 1000))
            if leftmost is None or a.min < leftmost:
                leftmost = a.min
            if rightmost is None or a.max > rightmost:
                rightmost = a.max
                tree.insert(a)
            self.assertEqual(set(), tree.query(leftmost - 1))
            self.assertEqual(set(), tree.query(rightmost + 1))

    def test_query_withPointInSomeIntervals_shouldReturnSetWithIntervalsThatContainQueryPoint(self):
        tree  = DynamicIntervalTree()
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
