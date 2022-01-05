from dataclasses import dataclass
from bindings.csw.conventional_unit_type import ConventionalUnitType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConventionalUnit(ConventionalUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
