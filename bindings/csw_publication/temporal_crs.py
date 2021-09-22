from dataclasses import dataclass
from bindings.csw_publication.temporal_crstype import TemporalCrstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCrs(TemporalCrstype):
    class Meta:
        name = "TemporalCRS"
        namespace = "http://www.opengis.net/gml"
