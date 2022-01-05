from dataclasses import dataclass
from bindings.gmd.geocentric_crsproperty_type import GeocentricCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrsref(GeocentricCrspropertyType):
    class Meta:
        name = "geocentricCRSRef"
        namespace = "http://www.opengis.net/gml"
