from src.abc.decomposable.binary_transform import BinaryTransform
from src.abc.decomposable.decomposable_sp  import DecomposableSP


class DynamicInsertion:

    def __init__(self, static, transform=None):
        if static is None:
            raise ValueError("Invalid argument 'static' of None Type")

        if type(static) != type(DecomposableSP):
            raise ValueError("Structure is not DecomposableSP")

        if transform is None:
            self.__transform = BinaryTransform()
        else:
            self.__transform = transform
        self.__transform.init(static)

    def __len__(self):
        return len(self.__transform)

    def insert(self, x):
        self.__transform.insert(x)

    def query(self, x):
        return self.__transform.query(x)

    def all(self):
        return self.__transform.all()
