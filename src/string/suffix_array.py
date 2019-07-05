from src.tree.suffix_tree import SuffixTree


class SuffixArray:

    def __init__(self, s):
        if s is None:
            raise ValueError("Invalid argument 's' of None type")
        self.__s = s
        self.__array = list()
        self.__build(self.__s)

    def __repr__(self):
        return repr(self.__array)

    def __str__(self):
        return str(self.__array)

    def __build(self, s):
        tree = SuffixTree(s)
        sequence = tree.root().f.keys_in_order()
        sequence.pop(0)

        for x in sequence:
            node = tree.root().f[x]
            self.__dfs(node, node.l, node.r)

    def __dfs(self, x, start, end):
        if len(x.f) == 0:
            self.__array.append(self.__s[start:end])
        for c in x.f.keys_in_order():
            if c == "$":
                self.__array.append(self.__s[start:end])
            else:
                self.__dfs(x.f[c], start, x.f[c].r)
