from dataclasses import dataclass
from bindings.csw.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CsId(IdentifierType):
    """
    An identification of a coordinate system.
    """
    class Meta:
        name = "csID"
        namespace = "http://www.opengis.net/gml"
