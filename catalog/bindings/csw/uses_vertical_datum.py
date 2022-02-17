from dataclasses import dataclass
from bindings.csw.vertical_datum_ref_type import VerticalDatumRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalDatum(VerticalDatumRefType):
    """
    Association to the vertical datum used by this CRS.
    """

    class Meta:
        name = "usesVerticalDatum"
        namespace = "http://www.opengis.net/gml"
