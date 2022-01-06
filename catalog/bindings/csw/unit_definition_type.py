from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.catalog_symbol import CatalogSymbol
from bindings.csw.definition_type import DefinitionType
from bindings.csw.quantity_type import QuantityType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UnitDefinitionType(DefinitionType):
    """Definition of a unit of measure (or uom).

    The definition includes a quantityType property, which indicates the
    phenomenon to which the units apply, and a catalogSymbol, which
    gives the short symbol used for this unit. This element is used when
    the relationship of this unit to other units or units systems is
    unknown.
    """

    quantity_type: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "quantityType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    catalog_symbol: Optional[CatalogSymbol] = field(
        default=None,
        metadata={
            "name": "catalogSymbol",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
