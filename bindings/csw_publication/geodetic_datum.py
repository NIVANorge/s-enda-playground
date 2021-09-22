from dataclasses import dataclass
from bindings.csw_publication.geodetic_datum_type import GeodeticDatumType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatum(GeodeticDatumType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
