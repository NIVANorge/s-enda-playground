from dataclasses import dataclass
from bindings.csw.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Definition(DefinitionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
