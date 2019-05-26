import unittest

from src.geometric.ds.priority_search_tree import PrioritySearchTree


class TestPrioritySearchTree(unittest.TestCase):

    def test_constructor_withNoneTypeArgumentData_shouldRaiseValueError(self):
        with self.assertRaises(ValueError):
            PrioritySearchTree(None)

