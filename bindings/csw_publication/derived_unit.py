from dataclasses import dataclass
from bindings.csw_publication.derived_unit_type import DerivedUnitType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedUnit(DerivedUnitType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
