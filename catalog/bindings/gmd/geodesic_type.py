from dataclasses import dataclass
from bindings.gmd.geodesic_string_type import GeodesicStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodesicType(GeodesicStringType):
    pass
