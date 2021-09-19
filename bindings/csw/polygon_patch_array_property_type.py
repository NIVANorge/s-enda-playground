from dataclasses import dataclass
from bindings.csw.surface_patch_array_property_type import SurfacePatchArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    This type defines a container for an array of polygon patches.
    """
