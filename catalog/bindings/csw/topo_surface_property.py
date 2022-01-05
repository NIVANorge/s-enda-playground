from dataclasses import dataclass
from bindings.csw.topo_surface_property_type import TopoSurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfaceProperty(TopoSurfacePropertyType):
    class Meta:
        name = "topoSurfaceProperty"
        namespace = "http://www.opengis.net/gml"
