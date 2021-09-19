from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw.metadata_1 import Metadata1

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class DomainType:
    """Valid domain (or set of values) of one parameter or other quantity used
    by this server.

    A non-parameter quantity may not be explicitly represented in the
    server software. (Informative: An example is the outputFormat
    parameter of a WFS. Each WFS server should provide a Parameter
    element for the outputFormat parameter that lists the supported
    output formats, such as GML2, GML3, etc. as the allowed "Value"
    elements.)

    :ivar value: Unordered list of all the valid values for this
        parameter or other quantity. For those parameters that contain a
        list or sequence of values, these values shall be for individual
        values in the list. The allowed set of values and the allowed
        server restrictions on that set of values shall be specified in
        the Implementation Specification for this service.
    :ivar metadata: Optional unordered list of additional metadata about
        this parameter. A list of required and optional metadata
        elements for this domain should be specified in the
        Implementation Specification for this service. (Informative:
        This metadata might specify the meanings of the valid values.)
    :ivar name: Name or identifier of this parameter or other quantity.
    """
    value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "min_occurs": 1,
        }
    )
    metadata: List[Metadata1] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
