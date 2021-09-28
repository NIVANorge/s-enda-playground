from dataclasses import dataclass
from bindings.wfs.literal_type import LiteralType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Literal(LiteralType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
