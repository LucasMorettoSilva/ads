from src.abc.decomposable.transform.binary_transform import BinaryTransform
from src.abc.decomposable.decomposable_sp  import DecomposableSP


class DynamicInsertionDeletion:

    def __init__(self, static, factor=0.5):
        if static is None:
            raise ValueError("Invalid argument 'static' of None Type")

        if type(static) != type(DecomposableSP):
            raise ValueError("Structure is not DecomposableSP")

        if factor >= 1:
            raise ValueError("Argument 'factor' must be in range (0, 1)")

        self.__factor = factor
        self.__static = static
        self.__real   = BinaryTransform()
        self.__ghost  = BinaryTransform()

        self.__real.init(static)
        self.__ghost.init(static)

    def __len__(self):
        return len(self.__real) - len(self.__ghost)

    def elements(self):
        active   = self.__real.all()
        inactive = self.__ghost.all()
        active.difference_update(inactive)
        return active

    def insert(self, x):
        self.__real.insert(x)

    def delete(self, x):
        if len(self.__ghost) > self.__factor * len(self.__real):
            self.__rebuild()
        self.__ghost.insert(x)

    def query(self, x):
        active   = self.__real.query(x)
        inactive = self.__ghost.query(x)
        return self.__static.operator_inverse(active, inactive)

    def __rebuild(self):
        active = self.elements()

        self.__real = BinaryTransform()
        self.__real.init(self.__static)
        for a in active:
            self.__real.insert(a)

        self.__ghost = BinaryTransform()
        self.__ghost.init(self.__static)
