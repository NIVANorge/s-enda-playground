from dataclasses import dataclass
from bindings.csw.literal_type import LiteralType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Literal(LiteralType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
