from dataclasses import dataclass
from bindings.csw_publication.geodesic_string_type import GeodesicStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodesicString(GeodesicStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
