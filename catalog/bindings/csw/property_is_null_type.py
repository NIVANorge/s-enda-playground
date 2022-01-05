from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.comparison_ops_type import ComparisonOpsType
from bindings.csw.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsNullType(ComparisonOpsType):
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        }
    )
