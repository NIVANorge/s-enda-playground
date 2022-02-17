from dataclasses import dataclass
from bindings.gmd.abstract_crstype import GeographicCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeographicCrsref(GeographicCrspropertyType):
    class Meta:
        name = "geographicCRSRef"
        namespace = "http://www.opengis.net/gml"
