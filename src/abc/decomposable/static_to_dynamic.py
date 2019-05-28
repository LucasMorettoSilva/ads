class StaticToDynamic:

    def __init__(self, struct, *args):
        if len(args) > 1:
            self._transform = args[0](struct)
        else:
            self._transform = args[0](struct)

    def __len__(self):
        return len(self._transform)

    def insert(self, x):
        self._transform.insert(x)

    def query(self, x):
        return self._transform.query(x)

    def all(self):
        return self._transform.all()
