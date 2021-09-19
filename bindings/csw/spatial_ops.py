from dataclasses import dataclass
from bindings.csw.spatial_ops_type import SpatialOpsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialOps(SpatialOpsType):
    class Meta:
        name = "spatialOps"
        namespace = "http://www.opengis.net/ogc"
