from src.abc.decomposable.transformation import Transformation


class BinaryTransform(Transformation):

    def __init__(self):
        super().__init__()
        self.__high = 0

    def insert(self, x):
        if x is None:
            raise ValueError("Illegal argument of None Type")

        if x in self._insertions:
            return

        self._insertions.add(x)
        s = set()
        s.add(x)

        i = 0
        while self._p[i] is not None:
            s.update(self._p[i].unbuild())
            self._p[i] = None
            i += 1
        self._p[i] = self._struct(s)
        if i == self.__high:
            self.__high += 1
            self._p.append(None)
