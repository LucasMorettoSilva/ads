import unittest

from src.string.suffix_array import SuffixArray


class TestSuffixArray(unittest.TestCase):

    def test_constructor(self):
        array = SuffixArray("banana")
        print(array)
