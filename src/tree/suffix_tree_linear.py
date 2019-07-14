from src.tree.avl_tree import AVLTree


class SuffixTreeLinear:

    class __Node:

        def __init__(self, l, r, p):
            self.l    = l
            self.r    = r
            self.p    = p
            self.suf  = None
            self.f    = AVLTree(self.__compare)
            self.size = 0

        def __len__(self):
            return self.r - self.l + 1

        def __repr__(self):
            return "[{}, {}]".format(self.l, self.r)

        @staticmethod
        def __compare(a, b):
            if a == "$" and b != "$":
                return -1
            if b == "$" and a != "$":
                return 1
            if a < b:
                return -1
            if a > b:
                return 1
            return 0

    def __init__(self, p):
        self.__p = p
        self.__r = self.__build(p)
        self.__update_fields(self.__r)
        self.__p += "$"

    def suffix_array(self):
        array = list()
        cur   = self.__r
        for key in cur.f:
            self.__dfs(cur.f[key], "", array)
        return array

    def __dfs(self, node, suf, array):
        if node.l == node.r:
            suf += self.__p[node.l:node.r + 1]
        else:
            suf += self.__p[node.l:node.r]
        if len(node.f) == 0:
            array.append(suf)
        else:
            for key in node.f:
                self.__dfs(node.f[key], suf, array)

    def root(self):
        return self.__r

    def __s(self, x, i):
        return self.__p[x.l + i]

    def __build_quad(self, p):
        r = self.__Node(1, 0, None)
        p += "$"
        for i in range(len(p)):
            cn = r
            cd = 0
            for j in range(i, len(p)):
                if cd == len(cn) and p[j] not in cn.f:
                    cn.f[p[j]] = self.__Node(j, len(p), cn)
                    break
                if cd < len(cn) and self.__s(cn, cd) != p[j]:
                    mid = self.__Node(cn.l, cn.l + cd, cn.p)
                    cn.p.f[self.__s(mid, 0)] = mid
                    mid.f[self.__s(cn, cd)] = cn
                    cn.p = mid
                    cn.l += cd
                    mid.f[p[j]] = self.__Node(j, len(p), mid)
                    break
                if cd == len(cn):
                    cn = cn.f[p[j]]
                    cd = 0
                cd += 1
        return r

    def __build(self, p):
        i = 0
        r = self.__Node(1, 0, None)
        p += "$"
        cn = r
        cd = 0
        ns = None
        for j in range(0, len(p)):
            while i <= j:
                if cd == len(cn) and p[j] in cn.f:
                    cn = cn.f[p[j]]
                    cd = 0
                if cd < len(cn) and self.__s(cn, cd) == p[j]:
                    cd += 1
                    break
                if cd == len(cn):
                    cn.f[p[j]] = self.__Node(j, len(p), cn)
                    if cn is not r:
                        cn = cn.suf
                        cd = len(cn)
                else:
                    mid = self.__Node(cn.l, cn.l + cd, cn.p)
                    cn.p.f[self.__s(mid, 0)] = mid
                    mid.f[self.__s(cn, cd)] = cn
                    cn.p = mid
                    cn.l += cd
                    mid.f[p[j]] = self.__Node(j, len(p), mid)
                    if ns is not None:
                        ns.suf = mid
                    cn = mid.p
                    if cn is not r:
                        cn = cn.suf
                        g  = j - cd
                    else:
                        g = i + 1
                    while g < j and g + len(cn.f[p[g]]) <= j:
                        cn = cn.f[p[g]]
                        g  += len(cn)
                    if g == j:
                        ns = None
                        mid.suf = cn
                        cd = len(cn)
                    else:
                        ns = mid
                        cn = cn.f[p[g]]
                        cd = j - g
                i += 1
        return r

    def __update_fields(self, x):
        if len(x.f) == 0:
            x.size = 1
        for c in x.f.keys_in_order():
            x.size += self.__update_fields(x.f[c])
        return x.size

    def check_pattern(self, s):
        return self.__find_match(s) is not None

    def find_match(self, s):
        match = self.__find_match(s)
        if s is None:
            return None
        return self.__p[match.l:match.r]

    def __find_match(self, s):
        cur = self.__r
        i = 0
        while i < len(s):
            if s[i] not in cur.f:
                return None

            cur = cur.f[s[i]]
            for c in self.__p[cur.l:cur.r+1]:
                if i >= len(s):
                    return cur
                if c == "$":
                    break
                if s[i] != c:
                    return None
                i += 1
        return cur

    def cont_occurrences(self, s):
        x = self.__find_match(s)
        if x is None:
            return 0
        return x.size

    def print(self):
        self.__print(self.__r)

    def __print(self, x):
        if x is self.__r:
            print("root")
        else:
            res = ""
            for i in range(x.l, x.r + 1):
                res += self.__p[i]
            print(res)

        children = []
        for c in x.f:
            if c == "$":
                children.append("$")
            else:
                children.append(self.__p[x.f[c].l:x.f[c].r+1])
        print(str(children) + "\n")

        for c in x.f:
            if c != "$":
                self.__print(x.f[c])
