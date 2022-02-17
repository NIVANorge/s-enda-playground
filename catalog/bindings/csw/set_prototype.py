from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.anim_named_target_attrs_attribute_type import (
    AnimNamedTargetAttrsAttributeType,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class SetPrototype:
    class Meta:
        name = "setPrototype"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        },
    )
    attribute_type: AnimNamedTargetAttrsAttributeType = field(
        default=AnimNamedTargetAttrsAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        },
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
