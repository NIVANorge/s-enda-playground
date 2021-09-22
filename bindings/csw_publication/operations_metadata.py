from dataclasses import dataclass, field
from typing import List, Optional
from bindings.csw_publication.domain_type import DomainType
from bindings.csw_publication.extended_capabilities import ExtendedCapabilities
from bindings.csw_publication.operation_1 import Operation1

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class OperationsMetadata:
    """Metadata about the operations and related abilities specified by this
    service and implemented by this server, including the URLs for operation
    requests.

    The basic contents of this section shall be the same for all OWS
    types, but individual services can add elements and/or change the
    optionality of optional elements.

    :ivar operation: Metadata for unordered list of all the (requests
        for) operations that this server interface implements. The list
        of required and optional operations implemented shall be
        specified in the Implementation Specification for this service.
    :ivar parameter: Optional unordered list of parameter valid domains
        that each apply to one or more operations which this server
        interface implements. The list of required and optional
        parameter domain limitations shall be specified in the
        Implementation Specification for this service.
    :ivar constraint: Optional unordered list of valid domain
        constraints on non-parameter quantities that each apply to this
        server. The list of required and optional constraints shall be
        specified in the Implementation Specification for this service.
    :ivar extended_capabilities:
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    operation: List[Operation1] = field(
        default_factory=list,
        metadata={
            "name": "Operation",
            "type": "Element",
            "min_occurs": 2,
        }
    )
    parameter: List[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
        }
    )
    constraint: List[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
        }
    )
    extended_capabilities: Optional[ExtendedCapabilities] = field(
        default=None,
        metadata={
            "name": "ExtendedCapabilities",
            "type": "Element",
        }
    )
