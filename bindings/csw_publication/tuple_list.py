from dataclasses import dataclass
from bindings.csw_publication.coordinates_type import CoordinatesType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TupleList(CoordinatesType):
    class Meta:
        name = "tupleList"
        namespace = "http://www.opengis.net/gml"
