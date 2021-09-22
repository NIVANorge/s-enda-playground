from dataclasses import dataclass
from bindings.csw_publication.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UnitDefinition(UnitDefinitionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
