from dataclasses import dataclass
from bindings.gmd.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionRef(ReferenceType):
    class Meta:
        name = "definitionRef"
        namespace = "http://www.opengis.net/gml"
