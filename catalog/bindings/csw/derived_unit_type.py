from dataclasses import dataclass, field
from typing import List
from bindings.csw.derivation_unit_term import DerivationUnitTerm
from bindings.csw.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedUnitType(UnitDefinitionType):
    """Definition of a unit of measure which is defined through algebraic
    combination of more primitive units, which are usually base units from a
    particular system of units.

    Derived units based directly on base units are usually preferred for
    quantities other than the base units or fundamental quantities
    within a system.  If a derived unit is not the preferred unit, the
    ConventionalUnit element should be used instead.
    """

    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
