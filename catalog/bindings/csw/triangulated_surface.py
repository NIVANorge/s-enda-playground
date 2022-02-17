from dataclasses import dataclass
from bindings.csw.triangulated_surface_type import TriangulatedSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TriangulatedSurface(TriangulatedSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
