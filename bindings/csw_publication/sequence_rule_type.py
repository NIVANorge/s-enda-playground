from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.increment_order import IncrementOrder
from bindings.csw_publication.sequence_rule_names import SequenceRuleNames

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SequenceRuleType:
    value: Optional[SequenceRuleNames] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    order: Optional[IncrementOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
