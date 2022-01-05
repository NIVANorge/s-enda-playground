from dataclasses import dataclass
from bindings.csw.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationId(IdentifierType):
    """
    An identification of a coordinate operation.
    """
    class Meta:
        name = "coordinateOperationID"
        namespace = "http://www.opengis.net/gml"
