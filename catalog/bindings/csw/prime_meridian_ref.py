from dataclasses import dataclass
from bindings.csw.prime_meridian_ref_type import PrimeMeridianRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianRef(PrimeMeridianRefType):
    class Meta:
        name = "primeMeridianRef"
        namespace = "http://www.opengis.net/gml"
