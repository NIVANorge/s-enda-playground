from dataclasses import dataclass
from bindings.csw.vertical_datum_type_1 import VerticalDatumType1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatum(VerticalDatumType1):
    class Meta:
        namespace = "http://www.opengis.net/gml"
