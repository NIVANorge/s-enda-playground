from dataclasses import dataclass
from bindings.csw_publication.binary_comparison_op_type import BinaryComparisonOpType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsGreaterThan(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
