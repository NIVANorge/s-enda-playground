from dataclasses import dataclass
from bindings.csw_publication.geocentric_crstype import GeocentricCrstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrs(GeocentricCrstype):
    class Meta:
        name = "GeocentricCRS"
        namespace = "http://www.opengis.net/gml"
