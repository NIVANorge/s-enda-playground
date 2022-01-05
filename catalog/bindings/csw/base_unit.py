from dataclasses import dataclass
from bindings.csw.base_unit_type import BaseUnitType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BaseUnit(BaseUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
