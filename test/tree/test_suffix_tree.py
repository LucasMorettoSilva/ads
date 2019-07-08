import unittest

from src.tree.suffix_tree import SuffixTree
from src.tree.trie        import Trie


class TestSuffixTree(unittest.TestCase):

    def test_checkPattern_withPatternInTree_shouldReturnTrue(self):
        pattern = "abcabbca"
        tree    = SuffixTree("abcabbca")
        for i in range(len(pattern)):
            for j in range(i, len(pattern) + 1):
                self.assertTrue(tree.check_pattern(pattern[i:j]))

        trie = Trie(pattern)
        for i in range(len(pattern)):
            self.assertIn(pattern[i:], trie)

    def test_checkPattern_withPatternNotInTree_shouldReturnFalse(self):
        # tree = SuffixTree("abracadabra")
        # tree.print()
        # self.assertFalse(tree.check_pattern("e"))
        # self.assertFalse(tree.check_pattern("nanan"))
        #
        trie = Trie("banana")
        print("match " + str(trie.match("m")))
        # print("find match " + str(trie.find_match("n")))
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

        trie = Trie("banana")
        self.assertEqual(0, trie.count("e"))
        self.assertEqual(0, trie.count("nanan"))
