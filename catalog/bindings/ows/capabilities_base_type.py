from dataclasses import dataclass, field
from typing import List, Optional
from bindings.ows.operations_metadata import OperationsMetadata
from bindings.ows.service_identification import ServiceIdentification
from bindings.ows.service_provider import ServiceProvider

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class CapabilitiesBaseType:
    """XML encoded GetCapabilities operation response.

    This document provides clients with service metadata about a
    specific service instance, usually including metadata about the
    tightly-coupled data served. If the server does not implement the
    updateSequence parameter, the server shall always return the
    complete Capabilities document, without the updateSequence
    parameter. When the server implements the updateSequence parameter
    and the GetCapabilities operation request included the
    updateSequence parameter with the current value, the server shall
    return this element with only the "version" and "updateSequence"
    attributes. Otherwise, all optional elements shall be included or
    not depending on the actual value of the Contents parameter in the
    GetCapabilities operation request. This base type shall be extended
    by each specific OWS to include the additional contents needed.

    :ivar service_identification:
    :ivar service_provider:
    :ivar operations_metadata:
    :ivar languages: The list of languages that this service is able to
        fully support. That is, if one of the listed languages is
        requested using the AcceptLanguages parameter in future requests
        to the server, all text strings contained in the response are
        guaranteed to be in that language. This list does not
        necessarily constitute a complete list of all languages that may
        be (at least partially) supported by the server. It only states
        the languages that are fully supported. If a server cannot
        guarantee full support of any particular language, it shall omit
        it from the list of supported languages in the capabilities
        document.
    :ivar version:
    :ivar update_sequence: Service metadata document version, having
        values that are "increased" whenever any change is made in
        service metadata document. Values are selected by each server,
        and are always opaque to clients. When not supported by server,
        server shall not return this attribute.
    """

    service_identification: Optional[ServiceIdentification] = field(
        default=None,
        metadata={
            "name": "ServiceIdentification",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    service_provider: Optional[ServiceProvider] = field(
        default=None,
        metadata={
            "name": "ServiceProvider",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    operations_metadata: Optional[OperationsMetadata] = field(
        default=None,
        metadata={
            "name": "OperationsMetadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    languages: Optional["CapabilitiesBaseType.Languages"] = field(
        default=None,
        metadata={
            "name": "Languages",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\d+\.\d?\d\.\d?\d",
        },
    )
    update_sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "updateSequence",
            "type": "Attribute",
        },
    )

    @dataclass
    class Languages:
        language: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Language",
                "type": "Element",
                "namespace": "http://www.opengis.net/ows/2.0",
                "min_occurs": 1,
            },
        )
