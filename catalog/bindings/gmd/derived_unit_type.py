from dataclasses import dataclass, field
from typing import List
from bindings.gmd.derivation_unit_term import DerivationUnitTerm
from bindings.gmd.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedUnitType(UnitDefinitionType):
    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
