from dataclasses import dataclass
from bindings.wfs.binary_spatial_op_type import BinarySpatialOpType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Overlaps(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
