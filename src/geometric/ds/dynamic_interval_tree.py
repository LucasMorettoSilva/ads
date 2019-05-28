from src.abc.decomposable.binary_transform   import BinaryTransform
from src.abc.decomposable.static_to_dynamic  import StaticToDynamic

from src.geometric.ds.interval_tree          import IntervalTree


class DynamicIntervalTree(StaticToDynamic):

    def __init__(self, t=BinaryTransform, k=None):
        if k is not None:
            super().__init__(IntervalTree, t, k)
        else:
            super().__init__(IntervalTree, t)
