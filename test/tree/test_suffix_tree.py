import unittest

from src.tree.suffix_tree import SuffixTree
from src.tree.trie        import Trie


class TestSuffixTree(unittest.TestCase):

    def test_checkPattern_withPatternInTree_shouldReturnTrue(self):
        pattern = "abcabbca"
        trie = Trie(pattern)
        for i in range(len(pattern)):
            self.assertIn(pattern[i:], trie)

    def test_checkPattern_withPatternNotInTree_shouldReturnFalse(self):
        trie = Trie("mississipi")
        self.assertNotIn("e", trie)
        self.assertNotIn("nanan", trie)

    def test_countOccurrences_withPatternInTree_shouldReturnNumberOfTimesPatternAppears(self):
        trie = Trie("banana")
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
        trie = Trie("banana")
        self.assertEqual(0, trie.count("e"))
        self.assertEqual(0, trie.count("nanan"))


