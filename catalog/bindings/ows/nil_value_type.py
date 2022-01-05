from dataclasses import dataclass, field
from typing import Optional
from bindings.ows.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class NilValueType(CodeType):
    """
    The value used (e.g. -255) to represent a nil value with optional nilReason
    and codeSpace attributes.

    :ivar nil_reason: An anyURI value which refers to a resource that
        describes the reason for the nil value
    """
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
        }
    )
