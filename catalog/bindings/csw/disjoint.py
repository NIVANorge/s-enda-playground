from dataclasses import dataclass
from bindings.csw.binary_spatial_op_type import BinarySpatialOpType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Disjoint(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
