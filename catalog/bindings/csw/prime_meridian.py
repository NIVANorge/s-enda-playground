from dataclasses import dataclass
from bindings.csw.prime_meridian_type import PrimeMeridianType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridian(PrimeMeridianType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
