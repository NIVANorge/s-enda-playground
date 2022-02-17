from dataclasses import dataclass
from bindings.csw.polygon_patch_type import PolygonPatchType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatch(PolygonPatchType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
