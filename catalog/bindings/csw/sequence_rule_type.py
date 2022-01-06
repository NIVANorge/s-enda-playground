from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.increment_order import IncrementOrder
from bindings.csw.sequence_rule_names import SequenceRuleNames

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SequenceRuleType:
    value: Optional[SequenceRuleNames] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    order: Optional[IncrementOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
