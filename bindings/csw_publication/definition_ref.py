from dataclasses import dataclass
from bindings.csw_publication.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionRef(ReferenceType):
    class Meta:
        name = "definitionRef"
        namespace = "http://www.opengis.net/gml"
