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

    def __contains__(self, pattern):
        x = self.__get(pattern)
        if x is None:
            return False
        return x.end

    def count(self, pattern):
        x = self.__get(pattern)
        if x is None:
            return 0
        return x.val

    def suffix_array(self):
        array = list()
        for char in self.__root.sub:
            # self.__find_string(self.__root.sub[char], "", array)
            self.__find_index(self.__root.sub[char], array)
        return array

    def lcp_array(self):
        suf_array = self.suffix_array()
        array     = [0] * len(suf_array)

        inv_suf = [0] * len(suf_array)
        for i in range(len(suf_array)):
            inv_suf[suf_array[i]] = i

        k = 0
        for i in range(len(suf_array)):
            if inv_suf[i] == len(suf_array) - 1:
                k = 0
                continue

            j = suf_array[inv_suf[i] + 1]
            while i + k < len(suf_array) and \
                  j + k < len(suf_array) and \
                  self.__txt[i + k] == self.__txt[j + k]:
                k += 1

            array[inv_suf[i]] = k
            if k > 0:
                k -= 1
        return array

    def __lcp(self, i, j, v, w):
        k = 0
        while i + k < len(v) and \
              j + k < len(w)          and \
              v[i + k] == w[j + k]:
            k += 1

        # cmp = 0
        # if w[b + k] < self.__txt[a + k]:
        #     cmp = -1
        # elif w[b + k] > self.__txt[a + k]:
        #     cmp = 1
        # else:
        #     cmp = 0
        return k

    def find_match(self, w):
        a = self.__txt
        pos = self.suffix_array()
        n = len(pos)
        p = len(w)

        L = 0
        R = n - 1
        l = self.__lcp(0, 0, a[pos[L:]], w)
        r = self.__lcp(0, 0, a[pos[R:]], w)
        while R - L > 1:
            M = (L + R) // 2
            m = a[pos[M:]]
            if l == r:
                j = self.__lcp(l + 1, l + 1, m, w)
                if l + j + 1 >= p or l + 1 + j >= len(m):
                    return M
                if w[l + 1 + j] < m[l + 1 + j]:
                    R = M
                    r = j - 1
                else:
                    L = M
                    l = j - 1
            elif l > r:
                lm = self.__lcp(0, 0, a[pos[L:]], a[pos[M:]])
                if lm < l:
                    R = M
                elif lm > l:
                    L = M

            if l >= r:
                if self.__lcp(pos[L], pos[M], a) >= l:
                    m = l + self.__lcp(pos[M] + l, l, w)
                else:
                    m = self.__lcp(pos[L], pos[M], a)
            else:
                if self.__lcp(pos[M], pos[R], a) >= r:
                    m = r + self.__lcp(pos[M] + r, r, w)
                else:
                    m = self.__lcp(pos[M], pos[R], a)
            if m == p or w[m] <= a[pos[M] + m]:
                R, r = M, m
            else:
                L, l = M, m
        lw = R
        return lw


    def match(self, w):
        a   = self.__txt
        pos = self.suffix_array()
        p   = len(w)
        n   = len(pos)
        l   = self.__lcp(pos[0], 0, w)
        r   = self.__lcp(pos[n - 1], 0, w)

        # if l == p or w[l] <= a[pos[0] + l]:
        #     lw = 0
        # elif r < p or w[r] <= a[pos[n - 1] + r]:
        #     lw = n
        # else:
        L = 0
        R = n - 1
        while R - L > 1:
            M = (L + R) // 2
            if l >= r:
                if self.__lcp(pos[L], pos[M], a) >= l:
                    m = l + self.__lcp(pos[M] + l, l, w)
                else:
                    m = self.__lcp(pos[L], pos[M], a)
            else:
                if self.__lcp(pos[M], pos[R], a) >= r:
                    m = r + self.__lcp(pos[M] + r, r, w)
                else:
                    m = self.__lcp(pos[M], pos[R], a)
            if m == p or w[m] <= a[pos[M] + m]:
                R, r = M, m
            else:
                L, l = M, m
        lw = R
        return lw

    def __find_string(self, node, suffix, array):
        if node.end:
            array.append(suffix + node.key)
        for char in node.sub:
            self.__find_string(node.sub[char], suffix + node.key, array)

    def __find_index(self, node, array):
        if node.end:
            array.append(node.idx)
        for char in node.sub:
            self.__find_index(node.sub[char], array)

    def __get(self, pattern):
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
