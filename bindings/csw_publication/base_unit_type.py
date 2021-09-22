from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.reference_type import ReferenceType
from bindings.csw_publication.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BaseUnitType(UnitDefinitionType):
    """Definition of a unit of measure which is a base unit from the system of
    units.

    A base unit cannot be derived by combination of other base units
    within this system.  Sometimes known as "fundamental unit".
    """
    units_system: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "unitsSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
