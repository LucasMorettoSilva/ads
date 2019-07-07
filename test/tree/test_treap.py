import random
import unittest

from src.tree.treap import Treap


class TestTreap(unittest.TestCase):

    def test_constructor_shouldCreateEmptySplayTree(self):
        bst = Treap()
        self.assertTrue(bst.empty())
        self.assertEqual(0, len(bst))
        self.assertEqual(-1, bst.height())

    def test_put_withNoneTypeArgumentKey_shouldRaiseValueError(self):
        bst = Treap()
        with self.assertRaises(ValueError):
            bst.put(None, 0)

    def test_setItem_withNoneTypeArgumentKey_shouldRaiseValueError(self):
        bst = Treap()
        with self.assertRaises(ValueError):
            bst[None] = 0

    def test_put_withNotEqualKeys_shouldInsertNewPairKeyValueIntoTree(self):
        bst = Treap()

        for i in range(1, 20):
            bst.put(i, str(i))
            print(str(bst.keys_level_order()))
            self.assertEqual(i, len(bst))

            self.assertIn(i, bst)
            self.assertEqual(str(i), bst[i])
            self.assertEqual(str(i), bst.get(i))

        for i in range(1, 20):
            self.assertIn(i, bst)
            self.assertEqual(str(i), bst[i])
            self.assertEqual(str(i), bst.get(i))

    def test_setItem_withNotEqualKeys_shouldInsertNewPairKeyValueIntoTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst[i] = str(i)
            self.assertEqual(i, len(bst))

            self.assertIn(i, bst)
            self.assertEqual(str(i), bst[i])
            self.assertEqual(str(i), bst.get(i))

        for i in range(1, 20):
            self.assertIn(i, bst)
            self.assertEqual(str(i), bst[i])
            self.assertEqual(str(i), bst.get(i))

    def test_put_withEqualKeys_shouldReplaceOldValueByNewValue(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(1, 20):
            self.assertEqual(str(i), bst.get(i))

            bst.put(i, str(i + 1))

            self.assertEqual(19, len(bst))
            self.assertIn(i, bst)
            self.assertEqual(str(i + 1), bst[i])
            self.assertEqual(str(i + 1), bst.get(i))

    def test_setItem_withEqualKeys_shouldReplaceOldValueByNewValue(self):
        bst = Treap()
        for i in range(1, 20):
            bst[i] = str(i)

        for i in range(1, 20):
            self.assertEqual(str(i), bst.get(i))

            bst[i] = str(i + 1)

            self.assertEqual(19, len(bst))
            self.assertIn(i, bst)
            self.assertEqual(str(i + 1), bst[i])
            self.assertEqual(str(i + 1), bst.get(i))

    def test_put_withNoneTypeArgumentValue_shouldDeleteKeyFromTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(1, 20):
            bst.put(i, None)

            self.assertEqual(19 - i, len(bst))
            self.assertNotIn(i, bst)

            for j in range(i + 1, 20):
                self.assertIn(j, bst)

    def test_setItem_withNoneTypeArgumentValue_shouldDeleteKeyFromTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst[i] = str(i)

        for i in range(1, 20):
            bst[i] = None

            self.assertEqual(19 - i, len(bst))
            self.assertNotIn(i, bst)

            for j in range(i + 1, 20):
                self.assertIn(j, bst)

    def test_delete_withNoneTypeArgumentKey_shouldRaiseValueError(self):
        bst = Treap()

        with self.assertRaises(ValueError):
            bst.delete(None)
        with self.assertRaises(ValueError):
            del bst[None]

    def test_delete_withKeyNotInTree_shouldNotModifyTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(20, 30):
            bst.delete(i)

            self.assertEqual(19, len(bst))
            for j in range(1, 20):
                self.assertIn(j, bst)

    def test_delete_withKeyInTree_shouldDeleteKeyFromTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(1, 20):
            bst.delete(i)

            self.assertEqual(19 - i, len(bst))
            self.assertNotIn(i, bst)
            for j in range(i + 1, 20):
                self.assertIn(j, bst)

    def test_get_withNoneTypeArgument_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            Treap().get(None)

    def test_get_withKeyNotInBST_shouldReturnNone(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(20, 30):
            self.assertIsNone(bst.get(i))

    def test_get_withKeyInBST_shouldReturnAssociatedValue(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(1, 20):
            self.assertEqual(str(i), bst.get(i))

    def test_getItem_withNoneTypeArgument_shouldRaiseValueError(self):
        bst = Treap()
        with self.assertRaises(ValueError):
            bst[None]

    def test_getItem_withKeyNotInBST_shouldReturnNone(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(20, 30):
            self.assertIsNone(bst[i])

    def test_getItem_withKeyInBST_shouldReturnAssociatedValue(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, str(i))

        for i in range(1, 20):
            self.assertEqual(str(i), bst[i])

    def test_min_withEmptyTree_shouldReturnNone(self):
        bst = Treap()
        self.assertIsNone(bst.min())

    def test_min_withNotEmptyTree_shouldReturnSmallestKeyFromTree(self):
        bst = Treap()
        for i in range(-1, -20, -1):
            bst.put(i, i)
            self.assertEqual(i, bst.min())

    def test_max_withEmptyTree_shouldReturnNone(self):
        bst = Treap()
        self.assertIsNone(bst.max())

    def test_max_withNotEmptyTree_shouldReturnLargestKeyFromTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, i)
            self.assertEqual(i, bst.max())

    def test_deleteMin_withEmptyTree_shouldNotModifyTree(self):
        bst = Treap()
        bst.delete_min()
        self.assertEqual(0, len(bst))
        self.assertEqual(-1, bst.height())

    def test_deleteMin_withNotEmptyTree_shouldDeleteSmallestKeyFromTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(i, i)
        for i in range(1, 20):
            bst.delete_min()
            self.assertEqual(19 - i, len(bst))
            self.assertNotIn(i, bst)
            for j in range(i + 1, 20):
                self.assertIn(j, bst)

    def test_deleteMax_withEmptyTree_shouldNotModifyTree(self):
        bst = Treap()
        bst.delete_max()
        self.assertEqual(0, len(bst))
        self.assertEqual(-1, bst.height())

    def test_deleteMax_withNotEmptyTree_shouldDeleteLargestKeyFromTree(self):
        bst = Treap()
        for i in range(1, 20):
            bst.put(-i, i)
        for i in range(1, 20):
            bst.delete_max()
            self.assertEqual(19 - i, len(bst))
            self.assertNotIn(-i, bst)
            for j in range(i + 1, 20):
                self.assertIn(-j, bst)

    def test_keysInOrder_withEmptyTree_shouldReturnEmptyList(self):
        bst = Treap()
        self.assertEqual([], bst.keys_in_order())

    def test_keysInOrder_withNotEmptyTree_shouldReturnListOfKeysInOrder(self):
        bst = Treap()
        inputs = random.sample(range(1, 1000), 100)

        for i in inputs:
            bst.put(i, i)

        self.assertEqual(sorted(inputs), bst.keys_in_order())
