from dataclasses import dataclass
from bindings.wfs.spatial_ops_type import SpatialOpsType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SpatialOps(SpatialOpsType):
    class Meta:
        name = "spatialOps"
        namespace = "http://www.opengis.net/fes/2.0"
