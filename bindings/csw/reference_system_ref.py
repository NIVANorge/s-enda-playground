from dataclasses import dataclass
from bindings.csw.reference_system_ref_type import ReferenceSystemRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ReferenceSystemRef(ReferenceSystemRefType):
    class Meta:
        name = "referenceSystemRef"
        namespace = "http://www.opengis.net/gml"
