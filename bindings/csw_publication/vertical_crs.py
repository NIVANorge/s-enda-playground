from dataclasses import dataclass
from bindings.csw_publication.vertical_crstype import VerticalCrstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCrs(VerticalCrstype):
    class Meta:
        name = "VerticalCRS"
        namespace = "http://www.opengis.net/gml"
