from dataclasses import dataclass
from bindings.csw.geodetic_datum_ref_type import GeodeticDatumRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesGeodeticDatum(GeodeticDatumRefType):
    """
    Association to the geodetic datum used by this CRS.
    """

    class Meta:
        name = "usesGeodeticDatum"
        namespace = "http://www.opengis.net/gml"
