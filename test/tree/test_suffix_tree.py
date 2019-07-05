import unittest

from src.tree.suffix_tree import SuffixTree


class TestSuffixTree(unittest.TestCase):

    def test_checkPattern_withPatternInTree_shouldReturnTrue(self):
        pattern = "banana"
        tree    = SuffixTree("banana")
        for i in range(len(pattern)):
            for j in range(i, len(pattern) + 1):
                self.assertTrue(tree.check_pattern(pattern[i:j]))

    def test_checkPattern_withPatternNotInTree_shouldReturnFalse(self):
        tree = SuffixTree("banana")
        self.assertFalse(tree.check_pattern("e"))
        self.assertFalse(tree.check_pattern("nanan"))

    def test_countOccurrences_withPatternInTree_shouldReturnNumberOfTimesPatternAppears(self):
        tree = SuffixTree("banana")
        self.assertEqual(1, tree.cont_occurrences("b"))
        self.assertEqual(1, tree.cont_occurrences("ba"))
        self.assertEqual(1, tree.cont_occurrences("ban"))
        self.assertEqual(1, tree.cont_occurrences("bana"))
        self.assertEqual(1, tree.cont_occurrences("banan"))
        self.assertEqual(1, tree.cont_occurrences("banana"))

        self.assertEqual(3, tree.cont_occurrences("a"))
        self.assertEqual(2, tree.cont_occurrences("an"))
        self.assertEqual(2, tree.cont_occurrences("ana"))
        self.assertEqual(1, tree.cont_occurrences("anan"))
        self.assertEqual(1, tree.cont_occurrences("anana"))

        self.assertEqual(2, tree.cont_occurrences("n"))
        self.assertEqual(2, tree.cont_occurrences("na"))
        self.assertEqual(1, tree.cont_occurrences("nan"))
        self.assertEqual(1, tree.cont_occurrences("nana"))

    def test_countOccurrences_withPatternNotInTree_shouldReturnZero(self):
        tree = SuffixTree("banana")
        self.assertEqual(0, tree.cont_occurrences("e"))
        self.assertEqual(0, tree.cont_occurrences("nanan"))
