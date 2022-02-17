from dataclasses import dataclass
from bindings.csw.geographic_crstype import GeographicCrstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeographicCrs(GeographicCrstype):
    class Meta:
        name = "GeographicCRS"
        namespace = "http://www.opengis.net/gml"
