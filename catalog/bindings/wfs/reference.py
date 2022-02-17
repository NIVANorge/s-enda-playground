from dataclasses import dataclass
from bindings.wfs.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
