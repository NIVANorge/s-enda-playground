from dataclasses import dataclass
from bindings.csw_publication.geographic_crsref_type import GeographicCrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeographicCrsref(GeographicCrsrefType):
    class Meta:
        name = "geographicCRSRef"
        namespace = "http://www.opengis.net/gml"
