from dataclasses import dataclass
from bindings.csw_publication.composite_surface_type import SurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ExtentOf(SurfacePropertyType):
    class Meta:
        name = "extentOf"
        namespace = "http://www.opengis.net/gml"
