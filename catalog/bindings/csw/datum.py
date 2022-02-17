from dataclasses import dataclass
from bindings.csw.abstract_datum_type import AbstractDatumType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Datum(AbstractDatumType):
    class Meta:
        name = "_Datum"
        namespace = "http://www.opengis.net/gml"
