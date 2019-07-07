import unittest

from src.string.suffix_array import SuffixArray

from src.tree.trie           import Trie


class TestSuffixArray(unittest.TestCase):

    def test_constructor(self):
        # array = SuffixArray("mississssipi")
        # print(array)

        trie = Trie("mississipi")
        print(trie.suffix_array)
        print(trie.find_match("mississipi"))
        # print(trie.lcp_array())

        # trie = Trie("lucas moretto da silva")
        # print(trie.suffix_array())
