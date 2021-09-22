from dataclasses import dataclass
from bindings.csw_publication.binary_spatial_op_type import BinarySpatialOpType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Touches(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
