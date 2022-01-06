from dataclasses import dataclass
from bindings.csw.identifier_type import IdentifierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GroupId(IdentifierType):
    """
    An identification of an operation parameter group.
    """

    class Meta:
        name = "groupID"
        namespace = "http://www.opengis.net/gml"
