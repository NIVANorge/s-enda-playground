from dataclasses import dataclass
from bindings.csw.vertical_datum_type_type import VerticalDatumTypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumType(VerticalDatumTypeType):
    class Meta:
        name = "verticalDatumType"
        namespace = "http://www.opengis.net/gml"
