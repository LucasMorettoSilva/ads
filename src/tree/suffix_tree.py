class SuffixTree:

    class __Node:

        def __init__(self, l, r, p):
            self.l   = l
            self.r   = r
            self.p   = p
            self.suf = None
            self.f   = dict()

        def __len__(self):
            return self.r - self.l + 1

        def __repr__(self):
            return "[{}, {}]".format(self.l, self.r)

    def __init__(self, p):
        self.__p = p + "$"
        self.__r = self.__Node(1, 0, None)
        self.__build()

    def __s(self, x, i):
        return self.__p[x.l + i]

    def __build(self):
        i = 0
        cn = self.__r
        cd = 0
        ns = None
        for j in range(0, len(self.__p)):
            while i <= j:
                if cd == len(cn) and self.__p[j] in cn.f:
                    cn = cn.f[self.__p[j]]
                    cd = 0
                if cd < len(cn) and self.__s(cn, cd) == self.__p[j]:
                    cd += 1
                    break
                if cd == len(cn):
                    cn.f[self.__p[j]] = self.__Node(j, len(self.__p), cn)
                    if cn is not self.__r:
                        cn = cn.suf
                        cd = len(cn)
                else:
                    mid = self.__Node(cn.l, cn.l + cd, cn.p)
                    cn.p.f[self.__s(mid, 0)] = mid
                    mid.f[self.__s(cn, cd)] = cn
                    cn.p = mid
                    cn.l += cd
                    mid.f[self.__p[j]] = self.__Node(j, len(self.__p), mid)
                    if ns is not None:
                        ns.suf = mid
                    cn = mid.p
                    if cn is not self.__r:
                        cn = cn.suf
                        g  = j - cd
                    else:
                        g = i + 1
                    while g < j and g + len(cn.f[self.__p[g]]) <= j:
                        cn = cn.f[self.__p[g]]
                        g  += len(cn)
                    if g == j:
                        ns = None
                        mid.suf = cn
                        cd = len(cn)
                    else:
                        ns = mid
                        cn = cn.f[self.__p[g]]
                        cd = j - g
                i += 1

    def check_pattern(self, s):
        cur = self.__r
        i = 0
        while i < len(s):
            if s[i] not in cur.f:
                return False

            cur = cur.f[s[i]]
            for c2 in self.__p[cur.l:cur.r]:
                if i >= len(s) or c2 == "$":
                    break
                if s[i] != c2:
                    return False
                i += 1
        return True






