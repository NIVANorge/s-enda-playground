from dataclasses import dataclass, field
from typing import Optional
from bindings.ows.un_named_domain_type import UnNamedDomainType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class DomainType(UnNamedDomainType):
    """
    Valid domain (or allowed set of values) of one quantity, with its name or
    identifier.

    :ivar name: Name or identifier of this quantity.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
