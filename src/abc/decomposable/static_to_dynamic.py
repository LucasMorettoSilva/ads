class StaticToDynamic:

    def __init__(self, struct, transform):
        self._transform = transform(struct)

    def __len__(self):
        return len(self._transform)

    def insert(self, x):
        self._transform.insert(x)

    def query(self, x):
        return self._transform.query(x)

    def all(self):
        return self._transform.all()
