from dataclasses import dataclass
from bindings.wfs.binary_comparison_op_type import BinaryComparisonOpType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsGreaterThanOrEqualTo(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
