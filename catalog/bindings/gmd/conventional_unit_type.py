from dataclasses import dataclass, field
from typing import List, Optional
from bindings.gmd.conversion_to_preferred_unit import ConversionToPreferredUnit
from bindings.gmd.derivation_unit_term import DerivationUnitTerm
from bindings.gmd.rough_conversion_to_preferred_unit import (
    RoughConversionToPreferredUnit,
)
from bindings.gmd.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConventionalUnitType(UnitDefinitionType):
    conversion_to_preferred_unit: Optional[ConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "conversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rough_conversion_to_preferred_unit: Optional[
        RoughConversionToPreferredUnit
    ] = field(
        default=None,
        metadata={
            "name": "roughConversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
