from dataclasses import dataclass, field
from typing import List, Optional
from generated.ows.pkg_1.pkg_0.pkg_0.ows19115subset import OnlineResourceType
from generated.ows.pkg_1.pkg_0.pkg_0.ows_common import Metadata

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class ExtendedCapabilities:
    """
    Individual software vendors and servers can use this element to provide
    metadata about any additional server abilities.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


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
    metadata: List[Metadata] = field(
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
            "namespace": "http://www.opengis.net/ows",
        }
    )


@dataclass
class Http:
    """Connect point URLs for the HTTP Distributed Computing Platform (DCP).

    Normally, only one Get and/or one Post is included in this element.
    More than one Get and/or Post is allowed to support including
    alternative URLs for uses such as load balancing or backup.

    :ivar get: Connect point URL prefix and any constraints for the HTTP
        "Get" request method for this operation request.
    :ivar post: Connect point URL and any constraints for the HTTP
        "Post" request method for this operation request.
    """
    class Meta:
        name = "HTTP"
        namespace = "http://www.opengis.net/ows"

    get: List[RequestMethodType] = field(
        default_factory=list,
        metadata={
            "name": "Get",
            "type": "Element",
        }
    )
    post: List[RequestMethodType] = field(
        default_factory=list,
        metadata={
            "name": "Post",
            "type": "Element",
        }
    )


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
        }
    )


@dataclass
class Operation:
    """
    Metadata for one operation that this server implements.

    :ivar dcp: Unordered list of Distributed Computing Platforms (DCPs)
        supported for this operation. At present, only the HTTP DCP is
        defined, so this element will appear only once.
    :ivar parameter: Optional unordered list of parameter domains that
        each apply to this operation which this server implements. If
        one of these Parameter elements has the same "name" attribute as
        a Parameter element in the OperationsMetadata element, this
        Parameter element shall override the other one for this
        operation. The list of required and optional parameter domain
        limitations for this operation shall be specified in the
        Implementation Specification for this service.
    :ivar constraint: Optional unordered list of valid domain
        constraints on non-parameter quantities that each apply to this
        operation. If one of these Constraint elements has the same
        "name" attribute as a Constraint element in the
        OperationsMetadata element, this Constraint element shall
        override the other one for this operation. The list of required
        and optional constraints for this operation shall be specified
        in the Implementation Specification for this service.
    :ivar metadata: Optional unordered list of additional metadata about
        this operation and its' implementation. A list of required and
        optional metadata elements for this operation should be
        specified in the Implementation Specification for this service.
        (Informative: This metadata might specify the operation request
        parameters or provide the XML Schemas for the operation
        request.)
    :ivar name: Name or identifier of this operation (request) (for
        example, GetCapabilities). The list of required and optional
        operations implemented shall be specified in the Implementation
        Specification for this service.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    dcp: List[Dcp] = field(
        default_factory=list,
        metadata={
            "name": "DCP",
            "type": "Element",
            "min_occurs": 1,
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
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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

    operation: List[Operation] = field(
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
