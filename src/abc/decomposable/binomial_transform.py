from src.abc.decomposable.transformation import Transformation


class BinomialTransform(Transformation):

    def __init__(self, struct, k=2):
        super().__init__(struct)
        self.__d = [0]
        self.__k = k

        for i in range(1, k + 1):
            self.__d.append(i - 1)
            self._p.append(None)
        self.__d.append(float("inf"))

    def insert(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        if x in self._insertions:
            return

        self._insertions.add(x)
        s = set()
        s.add(x)

        self.__d[1] = self.__d[1] + 1
        if self._p[1] is not None:
            s.update(self._p[1].unbuild())
            self._p[1] = None

        i = 1
        while self.__d[i] == self.__d[i + 1]:
            self.__d[i + 1] = self.__d[i + 1] + 1
            if self._p[i] is not None:
                s.update(self._p[i].unbuild())
            self._p[i]  = None
            self.__d[i] = i - 1
            i += 1
        self._p[i] = self._struct(s)
