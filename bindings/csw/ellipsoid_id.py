from dataclasses import dataclass
from bindings.csw.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidId(IdentifierType):
    """
    An identification of an ellipsoid.
    """
    class Meta:
        name = "ellipsoidID"
        namespace = "http://www.opengis.net/gml"
