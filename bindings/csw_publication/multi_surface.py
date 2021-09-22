from dataclasses import dataclass
from bindings.csw_publication.multi_surface_type import MultiSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurface(MultiSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
