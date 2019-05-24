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

    def test_notEquals_withNoneTypeArgument_shouldReturnTrue(self):
        p = Point2D(0, 0)
        self.assertNotEqual(p, None)

    def test_notEquals_withSamePoint_shouldReturnFalse(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            self.assertFalse(a != a)

    def test_notEquals_withSameInstance_shouldReturnFalse(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = a
            self.assertFalse(a != b)
            self.assertFalse(b != a)

    def test_notEquals_withEqualCoordinatePoints_shouldReturnFalse(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            c = Point2D(x, y)

            self.assertFalse(a != b)
            self.assertFalse(b != a)

            self.assertFalse(a != c)
            self.assertFalse(c != a)

            self.assertFalse(b != c)
            self.assertFalse(c != b)

    def test_notEquals_withNotEqualCoordinatePoints_shouldReturnTrue(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(-x, -y)
            self.assertTrue(a != b)
            self.assertTrue(b != a)

    def test_hash_withSameInstance_shouldReturnEqualHashCodes(self):
        for i in range(500):
            a = Point2D(random.uniform(0, 1000), random.uniform(0, 1000))
            b = a
            self.assertEqual(a, b)
            self.assertEqual(hash(a), hash(b))

    def test_hash_withEqualCoordinatePoints_shouldReturnEqualHashCodes(self):
        for i in range(500):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            self.assertEqual(a, b)
            self.assertEqual(hash(a), hash(b))

    def test_hash_withNotEqualCoordinatePoints_shouldReturnNotEqualHashCodes(self):
        for i in range(500):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(-x, -y)
            self.assertNotEqual(a, b)
            self.assertNotEqual(hash(a), hash(b))

    def test_distanceTo_withNoneTypeArgument_shouldRaiseValueError(self):
        p = Point2D(0, 0)
        with self.assertRaises(ValueError):
            p.distance_to(None)

    def test_distanceTo_withEqualPoints_shouldReturnZero(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            self.assertEqual(0, a.distance_to(b))
            self.assertEqual(0, b.distance_to(a))
            self.assertEqual(0, a.distance_to(a))

    def test_distanceTo_withNotEqualPoints_shouldReturnDistanceBetweenPoints(self):
        for i in range(1000):
            a = Point2D(random.uniform(0, 1000), random.uniform(0, 1000))
            b = Point2D(random.uniform(0, 1000), random.uniform(0, 1000))
            dx = a.x - b.x
            dy = a.y - b.y
            expected = math.sqrt(dx * dx + dy * dy)
            self.assertEqual(expected, a.distance_to(b))
            self.assertEqual(expected, b.distance_to(a))

    def test_distanceSquaredTo_withNoneTypeArgument_shouldRaiseValueError(self):
        p = Point2D(0, 0)
        with self.assertRaises(ValueError):
            p.distance_squared_to(None)

    def test_distanceSquaredTo_withEqualPoints_shouldReturnZero(self):
        for i in range(1000):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            self.assertEqual(0, a.distance_squared_to(b))
            self.assertEqual(0, b.distance_squared_to(a))
            self.assertEqual(0, a.distance_squared_to(a))

    def test_distanceSquaredTo_withNotEqualPoints_shouldReturnSquaredDistanceBetweenPoints(self):
        for i in range(1000):
            a = Point2D(random.uniform(0, 1000), random.uniform(0, 1000))
            b = Point2D(random.uniform(0, 1000), random.uniform(0, 1000))
            dx = a.x - b.x
            dy = a.y - b.y
            expected = dx * dx + dy * dy
            self.assertEqual(expected, a.distance_squared_to(b))
            self.assertEqual(expected, b.distance_squared_to(a))

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

    def test_xOrder_withEqualXCoordinatePoints_shouldReturnZero(self):
        for i in range(500):
            x = random.uniform(0, 1000)
            a = Point2D(x,  1)
            b = Point2D(x, -1)
            self.assertEqual(0, Point2D.x_order(a, b))
            self.assertEqual(0, Point2D.x_order(b, a))

    def test_xOrder_withNotEqualXCoordinatePoints_shouldReturnCorrectComparatorResult(self):
        for i in range(500):
            xa = random.uniform(0, 1000)
            xb = random.uniform(-1000, -1)
            a = Point2D(xa,  1)
            b = Point2D(xb, -1)
            self.assertEqual(1, Point2D.x_order(a, b))
            self.assertEqual(-1, Point2D.x_order(b, a))

    def test_yOrder_withEqualYCoordinatePoints_shouldReturnZero(self):
        for i in range(500):
            y = random.uniform(0, 1000)
            a = Point2D( 1, y)
            b = Point2D(-1, y)
            self.assertEqual(0, Point2D.y_order(a, b))
            self.assertEqual(0, Point2D.y_order(b, a))

    def test_yOrder_withNotEqualYCoordinatePoints_shouldReturnCorrectComparatorResult(self):
        for i in range(500):
            ya = random.uniform(0, 1000)
            yb = random.uniform(-1000, -1)
            a = Point2D( 1, ya)
            b = Point2D(-1, yb)
            self.assertEqual( 1, Point2D.y_order(a, b))
            self.assertEqual(-1, Point2D.y_order(b, a))

    def test_xyOrder_withEqualsXYCoordinatePoints_shouldReturnZero(self):
        for i in range(500):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            self.assertEqual(0, Point2D.xy_order(a, b))
            self.assertEqual(0, Point2D.xy_order(b, a))

    def test_xyOrder_withNotEqualXCoordinatePoints_shouldCompareByXAndReturnCorrectComparatorResult(self):
        for i in range(500):
            xa = random.uniform(0, 1000)
            xb = random.uniform(-1000, -1)
            a = Point2D(xa,  1)
            b = Point2D(xb, -1)
            self.assertEqual( 1, Point2D.xy_order(a, b))
            self.assertEqual(-1, Point2D.xy_order(b, a))

    def test_xyOrder_withEqualXAndNotEqualYCoordinatePoints_shouldCompareByYAndReturnCorrectComparatorResult(self):
        for i in range(500):
            ya = random.uniform(0, 1000)
            yb = random.uniform(-1000, -1)
            a = Point2D(1, ya)
            b = Point2D(1, yb)
            self.assertEqual( 1, Point2D.xy_order(a, b))
            self.assertEqual(-1, Point2D.xy_order(b, a))

    def test_yxOrder_withEqualsXYCoordinatePoints_shouldReturnZero(self):
        for i in range(500):
            x = random.uniform(0, 1000)
            y = random.uniform(0, 1000)
            a = Point2D(x, y)
            b = Point2D(x, y)
            self.assertEqual(0, Point2D.yx_order(a, b))
            self.assertEqual(0, Point2D.yx_order(b, a))

    def test_yxOrder_withNotEqualYCoordinatePoints_shouldCompareByYAndReturnCorrectComparatorResult(self):
        for i in range(500):
            ya = random.uniform(0, 1000)
            yb = random.uniform(-1000, -1)
            a = Point2D(1, ya)
            b = Point2D(1, yb)
            self.assertEqual(1, Point2D.yx_order(a, b))
            self.assertEqual(-1, Point2D.yx_order(b, a))

    def test_yxOrder_withEqualYAndNotEqualXCoordinatePoints_shouldCompareByXAndReturnCorrectComparatorResult(self):
        for i in range(500):
            xa = random.uniform(0, 1000)
            xb = random.uniform(-1000, -1)
            a = Point2D(xa, 1)
            b = Point2D(xb, 1)
            self.assertEqual(1, Point2D.yx_order(a, b))
            self.assertEqual(-1, Point2D.yx_order(b, a))
