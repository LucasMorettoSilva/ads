from src.tree.avl_tree import AVLTree


class Trie:

    class __Node:

        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.end = False
            self.idx = 0
            self.sub = AVLTree()

        def __repr__(self):
            return "[key: '{}', val: '{}', end: '{}']".format(
                self.key,
                self.val,
                self.end
            )

    def __init__(self, txt):
        if txt is None:
            raise ValueError("Illegal argument 'txt' of None type")
        self.__txt  = txt

        self.__root = self.__Node("", -1)
        self.__build()

        self.__sa   = self.__build_suffix_array()
        self.__lcp1 = self.__build_lcp()
        self.__llcp, self.__rlcp = self.__lcp_lr(self.__lcp1)

    def __contains__(self, pattern):
        x = self.__get_end_node(pattern)
        if x is None:
            return False
        return x.end

    def __build_lcp(self):
        n    = len(self.__sa)
        lcp  = [0] * n

        rank = [0] * n
        for i in range(n):
            rank[self.__sa[i]] = i

        k = 0
        for i in range(n):
            if rank[i] == n - 1:
                k = 0
                continue

            j = self.__sa[rank[i] + 1]
            while i + k < n and \
                  j + k < n and \
                  self.__txt[i + k] == self.__txt[j + k]:
                k += 1

            lcp[rank[i]] = k
            if k > 0:
                k -= 1
        return lcp

    def __build_suffix_array(self):
        suffix = list()
        for char in self.__root.sub:
            self.__find_index(self.__root.sub[char], suffix)
        return suffix

    def count(self, pattern):
        x = self.__get_end_node(pattern)
        if x is None:
            return 0
        return x.val

    @property
    def suffix_array(self):
        return self.__sa

    @property
    def lcp_array(self):
        return self.__lcp1

    @staticmethod
    def __lcp(i, j, v, w):
        k = 0
        while i + k < len(v) and \
                j + k < len(w) and \
                v[i + k] == w[j + k]:
            k += 1
        return k

    @staticmethod
    def __lcp_lr(lcp1):
        llcp, rlcp = [None] * len(lcp1), [None] * len(lcp1)
        lcp1 += [0]

        def precomputeLcpsHelper(l, r):
            if l == r - 1:    return lcp1[l]
            c = (l + r) // 2
            llcp[c - 1] = precomputeLcpsHelper(l, c)
            rlcp[c - 1] = precomputeLcpsHelper(c, r)
            return min(llcp[c - 1], rlcp[c - 1])

        precomputeLcpsHelper(0, len(lcp1))
        return llcp, rlcp

    def find_match(self, w):
        a   = self.__txt
        pos = self.suffix_array

        n = len(pos)
        p = len(w)

        L = 0
        R = n - 1
        l = self.__lcp(0, 0, a[pos[L]:], w)
        r = self.__lcp(0, 0, a[pos[R]:], w)
        while R - L > 1:
            M = (L + R) // 2
            m = a[pos[M]:]
            if l == r:
                j = self.__lcp(l, l, m, w)
                if l + j >= p:
                    return a[pos[M]:]
                if l + j < len(m) and w[l + j] < m[l + j]:
                    R = M
                    r = j
                else:
                    L = M
                    l = j
            elif l > r:
                lm = self.__llcp[M]
                if lm < l:
                    R = M
                elif lm > l:
                    L = M
                else:
                    j = self.__lcp(l, l, m, w)
                    if l + j >= p:
                        return a[pos[M]:]
                    if l + j < len(m) and w[l + j] < m[l + j]:
                        R = M
                        r = j
                    else:
                        L = M
                        l = j
            else:
                rm = self.__rlcp[M]
                if rm < r:
                    L = M
                elif rm > r:
                    R = M
                else:
                    j = self.__lcp(r, r, m, w)
                    if r + j >= p:
                        return a[pos[M]:]
                    if r + j < len(m) and w[r + j] < m[r + j]:
                        R = M
                        r = j
                    else:
                        L = M
                        l = j
        k = self.__lcp(0, 0, a[pos[R]:], w)
        if k < len(w):
            return -1
        return a[pos[R]:]

    # def match(self, w):
    #     a   = self.__txt
    #     pos = self.suffix_array()
    #     p   = len(w)
    #     n   = len(pos)
    #     l   = self.__lcp(pos[0], 0, w)
    #     r   = self.__lcp(pos[n - 1], 0, w)
    #
    #     # if l == p or w[l] <= a[pos[0] + l]:
    #     #     lw = 0
    #     # elif r < p or w[r] <= a[pos[n - 1] + r]:
    #     #     lw = n
    #     # else:
    #     L = 0
    #     R = n - 1
    #     while R - L > 1:
    #         M = (L + R) // 2
    #         if l >= r:
    #             if self.__lcp(pos[L], pos[M], a) >= l:
    #                 m = l + self.__lcp(pos[M] + l, l, w)
    #             else:
    #                 m = self.__lcp(pos[L], pos[M], a)
    #         else:
    #             if self.__lcp(pos[M], pos[R], a) >= r:
    #                 m = r + self.__lcp(pos[M] + r, r, w)
    #             else:
    #                 m = self.__lcp(pos[M], pos[R], a)
    #         if m == p or w[m] <= a[pos[M] + m]:
    #             R, r = M, m
    #         else:
    #             L, l = M, m
    #     lw = R
    #     return lw

    def __find_index(self, node, array):
        if node.end:
            array.append(node.idx)
        for char in node.sub:
            self.__find_index(node.sub[char], array)

    def __get_end_node(self, pattern):
        cur = self.__root
        for c in pattern:
            if c not in cur.sub:
                return None
            cur = cur.sub[c]
        return cur

    def __put(self, string, idx):
        cur = self.__root
        for c in string:
            if c not in cur.sub:
                cur.sub[c] = self.__Node(c, 0)
            cur = cur.sub[c]
            cur.val += 1
        cur.end = True
        cur.idx = idx

    def __build(self):
        for i in range(len(self.__txt)):
            self.__put(self.__txt[i:], i)
