from dataclasses import dataclass
from bindings.csw.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeridianId(IdentifierType):
    """
    An identification of a prime meridian.
    """

    class Meta:
        name = "meridianID"
        namespace = "http://www.opengis.net/gml"
