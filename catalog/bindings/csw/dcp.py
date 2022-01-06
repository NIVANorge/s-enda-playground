from dataclasses import dataclass, field
from typing import Optional
from bindings.csw.http import Http

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class Dcp:
    """Information for one distributed Computing Platform (DCP) supported for
    this operation.

    At present, only the HTTP DCP is defined, so this element only
    includes the HTTP element.
    """

    class Meta:
        name = "DCP"
        namespace = "http://www.opengis.net/ows"

    http: Optional[Http] = field(
        default=None,
        metadata={
            "name": "HTTP",
            "type": "Element",
        },
    )
