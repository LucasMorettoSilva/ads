from src.abc.decomposable.binary_transform   import BinaryTransform
from src.abc.decomposable.static_to_dynamic  import StaticToDynamic

from src.geometric.ds.interval_tree          import IntervalTree


class DynamicIntervalTree(StaticToDynamic):

    def __init__(self, t=None):
        if t is None:
            super().__init__(BinaryTransform(), IntervalTree)
        else:
            super().__init__(t, IntervalTree)
