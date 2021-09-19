from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.anim_add_accum_attrs_accumulate import AnimAddAccumAttrsAccumulate
from bindings.csw.anim_add_accum_attrs_additive import AnimAddAccumAttrsAdditive
from bindings.csw.anim_named_target_attrs_attribute_type import AnimNamedTargetAttrsAttributeType

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimatePrototype:
    class Meta:
        name = "animatePrototype"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        }
    )
    attribute_type: AnimNamedTargetAttrsAttributeType = field(
        default=AnimNamedTargetAttrsAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        }
    )
    additive: AnimAddAccumAttrsAdditive = field(
        default=AnimAddAccumAttrsAdditive.REPLACE,
        metadata={
            "type": "Attribute",
        }
    )
    accumulate: AnimAddAccumAttrsAccumulate = field(
        default=AnimAddAccumAttrsAccumulate.NONE,
        metadata={
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        }
    )
    by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    values: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
