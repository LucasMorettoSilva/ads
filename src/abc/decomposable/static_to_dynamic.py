class StaticToDynamic:

    def __init__(self, transform, static):
        if transform is None:
            raise ValueError("Invalid 'transform' of None Type")
        self._transform = transform
        self._transform.init(static)

    def __len__(self):
        return len(self._transform)

    def insert(self, x):
        self._transform.insert(x)

    def query(self, x):
        return self._transform.query(x)

    def all(self):
        return self._transform.all()
