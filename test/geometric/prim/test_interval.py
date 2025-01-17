import random
import unittest

from src.geometric.prim.interval import Interval


class TestInterval(unittest.TestCase):

    def test_constructor_shouldCreateIntervalBetweenGivenEndpoints(self):
        i = Interval(0, 1)
        self.assertEqual(0, i.min)
        self.assertEqual(1, i.max)
        self.assertEqual("[0, 1]", str(i))

        i = Interval(1, 0)
        self.assertEqual(0, i.min)
        self.assertEqual(1, i.max)
        self.assertEqual("[0, 1]", str(i))

    def test_hash_withEqualIntervals_shouldReturnEqualHashCodes(self):
        a = Interval(0, 1)
        b = Interval(0, 1)
        self.assertEqual(a, b)
        self.assertEqual(b, a)
        self.assertEqual(hash(a), hash(b))

        b = Interval(1, 0)
        self.assertEqual(a, b)
        self.assertEqual(b, a)
        self.assertEqual(hash(a), hash(b))

        b = a
        self.assertEqual(a, b)
        self.assertEqual(b, a)
        self.assertEqual(hash(a), hash(b))

    def test_hash_withNotEqualIntervals_shouldReturnNotEqualHashCodes(self):
        for _ in range(1000):
            a = Interval(random.uniform(1, 200), random.uniform(1, 200))
            b = Interval(random.uniform(1, 100), random.uniform(500, 1000))
            self.assertNotEqual(a, b)
            self.assertNotEqual(b, a)
            self.assertNotEqual(hash(a), hash(b))

    def test_equals_withNotEqualIntervals_shouldReturnFalse(self):
        a = Interval(0, 1)
        b = Interval(2, 0)
        self.assertFalse(a == b)
        self.assertFalse(b == a)

    def test_equals_withEqualIntervals_shouldReturnTrue(self):
        a = Interval(0, 1)
        b = Interval(1, 0)
        self.assertTrue(a == b)
        self.assertTrue(b == a)

        b = Interval(0, 1)
        self.assertTrue(a == b)
        self.assertTrue(b == a)

        b = a
        self.assertTrue(a == b)
        self.assertTrue(b == a)

    def test_notEquals_withNotEqualIntervals_shouldReturnTrue(self):
        a = Interval(0, 1)
        b = Interval(2, 0)
        self.assertTrue(a != b)
        self.assertTrue(b != a)

    def test_notEquals_withEqualIntervals_shouldReturnFalse(self):
        a = Interval(0, 1)
        b = Interval(1, 0)
        self.assertFalse(a != b)
        self.assertFalse(b != a)

        b = Interval(0, 1)
        self.assertFalse(a != b)
        self.assertFalse(b != a)

        b = a
        self.assertFalse(a != b)
        self.assertFalse(b != a)

    def test_contains_withPointNotInInterval_shouldReturnFalse(self):
        i = Interval(0, 1)
        for _ in range(1000):
            a = random.random() + 1.1
            b = random.random() - 1
            self.assertFalse(i.contains(a))
            self.assertFalse(a in i)
            self.assertFalse(i.contains(b))
            self.assertFalse(b in i)

    def test_contains_withPointInInterval_shouldReturnTrue(self):
        i = Interval(0, 1)

        self.assertTrue(i.contains(0))
        self.assertTrue(i.contains(1))
        self.assertTrue(0 in i)
        self.assertTrue(1 in i)

        for _ in range(1000):
            a = random.random()
            self.assertTrue(i.contains(a))
            self.assertTrue(a in i)

    def test_intersects_withIntervalsThatDoNotIntersect_shouldReturnFalse(self):
        for _ in range(1000):
            # Interval in range [0, 1)
            a = Interval(random.uniform(0, 1), random.uniform(0, 1))

            # Interval in range [1, 1000)
            b = Interval(random.uniform(1, 1000), random.uniform(1, 1000))

            # Interval in range [-1000, -0.1)
            c = Interval(random.uniform(-0.1, -1000), random.uniform(-0.1, -1000))

            self.assertFalse(a.intersects(b))
            self.assertFalse(a.intersects(c))
            self.assertFalse(b.intersects(c))

    def test_intersects_withIntervalsThatDoIntersect_shouldReturnTrue(self):
        i = Interval(0, 3)
        for _ in range(1000):
            a = Interval(random.uniform(1, 2), random.uniform(1, 2))
            self.assertTrue(i.intersects(a))

    def test_minOrder_withIntervalsWithNotEqualMinEndpoint_shouldCompareByMinEndpoint(self):
        for _ in range(1000):
            a = Interval(random.uniform(1, 200), random.uniform(1, 200))
            b = Interval(random.uniform(500, 1000), random.uniform(500, 1000))
            self.assertEqual(-1, Interval.min_order(a, b))
            self.assertEqual(1,  Interval.min_order(b, a))

    def test_minOrder_withIntervalsWithEqualMinEndpointAndNotEqualMaxEndpoint_shouldCompareByMaxEndpoint(self):
        for _ in range(1000):
            a = Interval(0, random.uniform(1, 200))
            b = Interval(0, random.uniform(500, 1000))
            self.assertEqual(-1, Interval.min_order(a, b))
            self.assertEqual(1,  Interval.min_order(b, a))

    def test_minOrder_withEqualIntervals_shouldReturnZero(self):
        a = Interval(1, 0)
        b = Interval(1, 0)
        self.assertEqual(0, Interval.min_order(a, b))
        self.assertEqual(0, Interval.min_order(b, a))

        b = Interval(0, 1)
        self.assertEqual(0, Interval.min_order(a, b))
        self.assertEqual(0, Interval.min_order(b, a))

        b = a
        self.assertEqual(0, Interval.min_order(a, b))
        self.assertEqual(0, Interval.min_order(b, a))

    def test_maxOrder_withIntervalsWithNotEqualMaxEndpoint_shouldCompareByMaxEndpoint(self):
        for _ in range(1000):
            a = Interval(random.uniform(1, 200), random.uniform(1, 200))
            b = Interval(random.uniform(500, 1000), random.uniform(500, 1000))
            self.assertEqual(-1, Interval.max_order(a, b))
            self.assertEqual(1,  Interval.max_order(b, a))

    def test_maxOrder_withIntervalsWithEqualMaxEndpointAndNotEqualMinEndpoint_shouldCompareByMinEndpoint(self):
        for _ in range(1000):
            a = Interval(random.uniform(1, 200), 1500)
            b = Interval(random.uniform(500, 1000), 1500)
            self.assertEqual(-1, Interval.max_order(a, b))
            self.assertEqual(1,  Interval.max_order(b, a))

    def test_maxOrder_withEqualIntervals_shouldReturnZero(self):
        a = Interval(1, 0)
        b = Interval(1, 0)
        self.assertEqual(0, Interval.max_order(a, b))
        self.assertEqual(0, Interval.max_order(b, a))

        b = Interval(0, 1)
        self.assertEqual(0, Interval.max_order(a, b))
        self.assertEqual(0, Interval.max_order(b, a))

        b = a
        self.assertEqual(0, Interval.max_order(a, b))
        self.assertEqual(0, Interval.max_order(b, a))

    def test_lengthOrder_withIntervalsWithNotEqualLength_shouldReturnCorrectComparator(self):
        for _ in range(1000):
            a = Interval(random.uniform(1, 200), random.uniform(1, 200))
            b = Interval(random.uniform(1, 100), random.uniform(500, 1000))
            self.assertEqual(-1, Interval.length_order(a, b))
            self.assertEqual(1,  Interval.length_order(b, a))

    def test_lengthOrder_withEqualLengthIntervals_shouldReturnZero(self):
        a = Interval(1, 0)
        b = Interval(1, 0)
        self.assertEqual(0, Interval.length_order(a, b))
        self.assertEqual(0, Interval.length_order(b, a))

        b = Interval(0, 1)
        self.assertEqual(0, Interval.length_order(a, b))
        self.assertEqual(0, Interval.length_order(b, a))

        b = a
        self.assertEqual(0, Interval.length_order(a, b))
        self.assertEqual(0, Interval.length_order(b, a))
