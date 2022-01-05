from dataclasses import dataclass
from bindings.csw.topo_point_type import TopoPointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPoint(TopoPointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
