from dataclasses import dataclass
from bindings.csw_publication.multi_surface_property_type import MultiSurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiExtentOf(MultiSurfacePropertyType):
    class Meta:
        name = "multiExtentOf"
        namespace = "http://www.opengis.net/gml"
