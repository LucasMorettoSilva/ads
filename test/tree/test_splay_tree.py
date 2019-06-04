import unittest

from src.tree.splay_tree import SplayTree


class TestSplayTree(unittest.TestCase):

    def test_constructor_shouldCreateEmptySplayTree(self):
        bst = SplayTree()
        self.assertEqual(0, len(bst))
        self.assertEqual(-1, bst.height())

