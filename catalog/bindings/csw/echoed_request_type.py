from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/cat/csw/2.0.2"


@dataclass
class EchoedRequestType:
    """
    Includes a copy of the request message body.
    """
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
