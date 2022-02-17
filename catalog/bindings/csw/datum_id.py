from dataclasses import dataclass
from bindings.csw.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DatumId(IdentifierType):
    """
    An identification of a datum.
    """

    class Meta:
        name = "datumID"
        namespace = "http://www.opengis.net/gml"
