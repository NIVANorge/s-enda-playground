from dataclasses import dataclass
from bindings.csw_publication.surface_patch_array_property_type import SurfacePatchArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrianglePatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    This type defines a container for an array of triangle patches.
    """
