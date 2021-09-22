from dataclasses import dataclass
from bindings.csw_publication.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Reference(ReferenceType):
    class Meta:
        name = "_reference"
        namespace = "http://www.opengis.net/gml"
