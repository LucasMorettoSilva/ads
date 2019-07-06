from src.tree.suffix_tree import SuffixTree
from src.tree.trie        import Trie


class SuffixArray:

    def __init__(self, s):
        if s is None:
            raise ValueError("Invalid argument 's' of None type")
        self.__s = s
        self.__array = list()
        self.__build2(self.__s)

    def __repr__(self):
        return repr(self.__array)

    def __str__(self):
        return str(self.__array)

    def __build2(self, s):
        tree  = SuffixTree(s)
        begin = tree.root().f.keys_in_order()
        for b in begin:
            node = tree.root().f[b]
            if node.l == node.r:
                self.__dfs2(node, s[node.l])
            else:
                self.__dfs2(node, s[node.l:node.r])

    def __dfs2(self, x, suffix):
        chars = x.f.keys_in_order()
        if len(chars) == 0:
            self.__array.append(suffix)
            return
        for c in chars:
            node = x.f[c]
            self.__dfs2(node, suffix + self.__s[node.l:node.r])
