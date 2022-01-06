from dataclasses import dataclass
from bindings.csw.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SrsId(IdentifierType):
    """
    An identification of a reference system.
    """

    class Meta:
        name = "srsID"
        namespace = "http://www.opengis.net/gml"
