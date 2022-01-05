from dataclasses import dataclass
from bindings.csw.polyhedral_surface_type import PolyhedralSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolyhedralSurface(PolyhedralSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
