from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.comparison_ops_type import ComparisonOpsType
from bindings.csw_publication.literal import Literal
from bindings.csw_publication.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsLikeType(ComparisonOpsType):
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
    wild_card: Optional[str] = field(
        default=None,
        metadata={
            "name": "wildCard",
            "type": "Attribute",
            "required": True,
        }
    )
    single_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "singleChar",
            "type": "Attribute",
            "required": True,
        }
    )
    escape_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "escapeChar",
            "type": "Attribute",
            "required": True,
        }
    )
    match_case: bool = field(
        default=True,
        metadata={
            "name": "matchCase",
            "type": "Attribute",
        }
    )
