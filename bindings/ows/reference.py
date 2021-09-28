from dataclasses import dataclass
from bindings.ows.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
