import math
import random
import unittest

from src.geometric.prim.point_2d import Point2D


class TestPoint2D(unittest.TestCase):

    def test_constructor_withNoneTypeArgumentX_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            Point2D(None, 0)

    def test_constructor_withNoneTypeArgumentY_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            Point2D(0, None)

    def test_constructor_withInfiniteCoordinateX_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            Point2D(float("inf"), 0)
        with self.assertRaises(ValueError):
            Point2D(float("-inf"), 0)

    def test_constructor_withInfiniteCoordinateY_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            Point2D(0, float("inf"))
        with self.assertRaises(ValueError):
            Point2D(0, float("-inf"))

    def test_constructor_withNaNCoordinateX_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            Point2D(float("NaN"), 0)

    def test_constructor_withNaNCoordinateY_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            Point2D(0, float("NaN"))

    def test_constructor_withValidXY_shouldCreatePointWithGivenCoordinates(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            p = Point2D(x, y)
            self.assertEqual(x, p.x)
            self.assertEqual(y, p.y)
            self.assertEqual(math.atan2(y, x), p.theta)
            self.assertEqual(math.sqrt(x ** 2 + y ** 2), p.r)
            self.assertEqual("({}, {})".format(x, y), str(p))

    def test_constructor_withDifferentZeros_shouldEliminateAmbiguitiesInInput(self):
        p = Point2D(-0, 0)
        self.assertEqual(0, p.x)
        self.assertEqual(0, p.y)
        self.assertEqual(p.x, p.y)

        p = Point2D(0, -0)
        self.assertEqual(0, p.x)
        self.assertEqual(0, p.y)
        self.assertEqual(p.x, p.y)

        p = Point2D(-0, -0)
        self.assertEqual(0, p.x)
        self.assertEqual(0, p.y)
        self.assertEqual(p.x, p.y)

        p = Point2D(-0, +0)
        self.assertEqual(0, p.x)
        self.assertEqual(0, p.y)
        self.assertEqual(p.x, p.y)

        p = Point2D(+0, -0)
        self.assertEqual(0, p.x)
        self.assertEqual(0, p.y)
        self.assertEqual(p.x, p.y)

        p = Point2D(+0, +0)
        self.assertEqual(0, p.x)
        self.assertEqual(0, p.y)
        self.assertEqual(p.x, p.y)

        a = Point2D(-0, -0)
        b = Point2D(+0, +0)
        self.assertEqual(a.x, b.x)
        self.assertEqual(a.y, b.y)
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))

    def test_equals_withNoneTypeArgument_shouldReturnFalse(self):
        p = Point2D(0, 0)
        self.assertNotEqual(p, None)

    def test_equals_withNotEqualCoordinatePoints_shouldReturnFalse(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(-x, -y)
            self.assertFalse(a == b)
            self.assertFalse(b == a)

    def test_equals_withSamePoint_shouldReturnTrue(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            self.assertEqual(a, a)

    def test_equals_withSameInstance_shouldReturnTrue(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = a
            self.assertEqual(a, b)
            self.assertEqual(b, a)

    def test_equals_withEqualCoordinatePoints_shouldReturnTrue(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            c = Point2D(x, y)

            self.assertEqual(a, b)
            self.assertEqual(b, a)

            self.assertEqual(a, c)
            self.assertEqual(c, a)

            self.assertEqual(b, c)
            self.assertEqual(c, b)

    def test_angleTo_withNoneTypeArgument_shouldRaiseValueError(self):
        p = Point2D(0, 0)
        with self.assertRaises(ValueError):
            p.angle_to(None)

    def test_angleTo_withEqualPoints_shouldReturnZero(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            self.assertEqual(0, a.angle_to(b))
