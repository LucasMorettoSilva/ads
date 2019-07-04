import unittest

from src.tree.suffix_tree import SuffixTree


class TestSuffixTree(unittest.TestCase):

    def test_checkPattern_withPatternInTree_shouldReturnTrue(self):
        pattern = "banana"
        tree    = SuffixTree("banana")
        for i in range(len(pattern)):
            for j in range(i, len(pattern) + 1):
                self.assertTrue(tree.check_pattern(pattern[i:j]))





