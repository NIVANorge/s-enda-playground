from dataclasses import dataclass
from bindings.gmd.triangle_patch_array_property_type import TrianglePatchArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrianglePatches(TrianglePatchArrayPropertyType):
    class Meta:
        name = "trianglePatches"
        namespace = "http://www.opengis.net/gml"
