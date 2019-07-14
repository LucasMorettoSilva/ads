import unittest

from src.tree.suffix_tree_linear import SuffixTreeLinear
from src.tree.suffix_tree        import SuffixTree


class TestSuffixTree(unittest.TestCase):

    def test_checkPattern_withPatternInTree_shouldReturnTrue(self):
        pattern = "abcabbca"
        trie = SuffixTree(pattern)
        for i in range(len(pattern)):
            self.assertIn(pattern[i:], trie)

    def test_checkPattern_withPatternNotInTree_shouldReturnFalse(self):
        trie = SuffixTree("mississipi")
        self.assertNotIn("e", trie)
        self.assertNotIn("nanan", trie)

    def test_countOccurrences_withPatternInTree_shouldReturnNumberOfTimesPatternAppears(self):
        trie = SuffixTree("banana")
        self.assertEqual(1, trie.count("b"))
        self.assertEqual(1, trie.count("ba"))
        self.assertEqual(1, trie.count("ban"))
        self.assertEqual(1, trie.count("bana"))
        self.assertEqual(1, trie.count("banan"))
        self.assertEqual(1, trie.count("banana"))

        self.assertEqual(3, trie.count("a"))
        self.assertEqual(2, trie.count("an"))
        self.assertEqual(2, trie.count("ana"))
        self.assertEqual(1, trie.count("anan"))
        self.assertEqual(1, trie.count("anana"))

        self.assertEqual(2, trie.count("n"))
        self.assertEqual(2, trie.count("na"))
        self.assertEqual(1, trie.count("nan"))
        self.assertEqual(1, trie.count("nana"))

    def test_countOccurrences_withPatternNotInTree_shouldReturnZero(self):
        trie = SuffixTree("banana")
        self.assertEqual(0, trie.count("e"))
        self.assertEqual(0, trie.count("nanan"))


