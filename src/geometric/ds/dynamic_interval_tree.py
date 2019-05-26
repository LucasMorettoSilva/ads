from src.abc.decomposable.binary_transform   import BinaryTransform
from src.abc.decomposable.binomial_transform import BinomialTransform
from src.abc.decomposable.static_to_dynamic  import StaticToDynamic

from src.geometric.ds.interval_tree          import IntervalTree


class DynamicIntervalTree(StaticToDynamic):

    def __init__(self, t=BinaryTransform):
        super().__init__(IntervalTree, t)
