from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class ExceptionType:
    """
    An Exception element describes one detected error that a server chooses to
    convey to the client.

    :ivar exception_text: Ordered sequence of text strings that describe
        this specific exception or error. The contents of these strings
        are left open to definition by each server implementation. A
        server is strongly encouraged to include at least one
        ExceptionText value, to provide more information about the
        detected error than provided by the exceptionCode. When
        included, multiple ExceptionText values shall provide
        hierarchical information about one detected error, with the most
        significant information listed first.
    :ivar exception_code: A code representing the type of this
        exception, which shall be selected from a set of exceptionCode
        values specified for the specific service operation and server.
    :ivar locator: When included, this locator shall indicate to the
        client where an exception was encountered in servicing the
        client's operation request. This locator should be included
        whenever meaningful information can be provided by the server.
        The contents of this locator will depend on the specific
        exceptionCode and OWS service, and shall be specified in the OWS
        Implementation Specification.
    """
    exception_text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ExceptionText",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    exception_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "exceptionCode",
            "type": "Attribute",
            "required": True,
        }
    )
    locator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Exception(ExceptionType):
    class Meta:
        namespace = "http://www.opengis.net/ows"


@dataclass
class ExceptionReport:
    """
    Report message returned to the client that requested any OWS operation when
    the server detects an error while processing that operation request.

    :ivar exception: Unordered list of one or more Exception elements
        that each describes an error. These Exception elements shall be
        interpreted by clients as being independent of one another (not
        hierarchical).
    :ivar version: Specification version for OWS operation. The string
        value shall contain one x.y.z "version" value (e.g., "2.1.3"). A
        version number shall contain three non-negative integers
        separated by decimal points, in the form "x.y.z". The integers y
        and z shall not exceed 99. Each version shall be for the
        Implementation Specification (document) and the associated XML
        Schemas to which requested operations will conform. An
        Implementation Specification version normally specifies XML
        Schemas against which an XML encoded operation response must
        conform and should be validated. See Version negotiation
        subclause for more information.
    :ivar language: Identifier of the language used by all included
        exception text values. These language identifiers shall be as
        specified in IETF RFC 1766. When this attribute is omitted, the
        language used is not identified.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows"

    exception: List[Exception] = field(
        default_factory=list,
        metadata={
            "name": "Exception",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
