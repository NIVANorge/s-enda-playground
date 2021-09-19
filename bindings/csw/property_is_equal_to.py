from dataclasses import dataclass
from bindings.csw.binary_comparison_op_type import BinaryComparisonOpType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsEqualTo(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
