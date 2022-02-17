from dataclasses import dataclass
from bindings.csw.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Surface1(SurfaceType):
    class Meta:
        name = "Surface"
        namespace = "http://www.opengis.net/gml"
