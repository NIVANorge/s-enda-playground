from dataclasses import dataclass
from bindings.csw_publication.topo_surface_type import TopoSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurface(TopoSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
