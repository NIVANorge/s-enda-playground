from dataclasses import dataclass, field
from typing import List
from bindings.wfs.domain_type import DomainType
from bindings.wfs.online_resource_type import OnlineResourceType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class RequestMethodType(OnlineResourceType):
    """Connect point URL and any constraints for this HTTP request method for
    this operation request.

    In the OnlineResourceType, the xlink:href attribute in the
    xlink:simpleAttrs attribute group shall be used to contain this URL.
    The other attributes in the xlink:simpleAttrs attribute group should
    not be used.

    :ivar constraint: Optional unordered list of valid domain
        constraints on non-parameter quantities that each apply to this
        request method for this operation. If one of these Constraint
        elements has the same "name" attribute as a Constraint element
        in the OperationsMetadata or Operation element, this Constraint
        element shall override the other one for this operation. The
        list of required and optional constraints for this request
        method for this operation shall be specified in the
        Implementation Specification for this service.
    """
    constraint: List[DomainType] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        }
    )
