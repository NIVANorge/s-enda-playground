from dataclasses import dataclass, field
from typing import List, Optional
from generated.ows.pkg_1.pkg_0.pkg_0.ows_operations_metadata import OperationsMetadata
from generated.ows.pkg_1.pkg_0.pkg_0.ows_service_identification import ServiceIdentification
from generated.ows.pkg_1.pkg_0.pkg_0.ows_service_provider import ServiceProvider

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class AcceptFormatsType:
    """Prioritized sequence of zero or more GetCapabilities operation response
    formats desired by client, with preferred formats listed first.

    Each response format shall be identified by its MIME type. See
    AcceptFormats parameter use subclause for more information.
    """
    output_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OutputFormat",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        }
    )


@dataclass
class AcceptVersionsType:
    """Prioritized sequence of one or more specification versions accepted by
    client, with preferred versions listed first.

    See Version negotiation subclause for more information.
    """
    version: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "min_occurs": 1,
        }
    )


@dataclass
class SectionsType:
    """Unordered list of zero or more names of requested sections in complete
    service metadata document.

    Each Section value shall contain an allowed section name as
    specified by each OWS specification. See Sections parameter
    subclause for more information.
    """
    section: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Section",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )


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
    """
    service_identification: Optional[ServiceIdentification] = field(
        default=None,
        metadata={
            "name": "ServiceIdentification",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    service_provider: Optional[ServiceProvider] = field(
        default=None,
        metadata={
            "name": "ServiceProvider",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    operations_metadata: Optional[OperationsMetadata] = field(
        default=None,
        metadata={
            "name": "OperationsMetadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    update_sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "updateSequence",
            "type": "Attribute",
        }
    )


@dataclass
class GetCapabilitiesType:
    """XML encoded GetCapabilities operation request.

    This operation allows clients to retrieve service metadata about a
    specific service instance. In this XML encoding, no "request"
    parameter is included, since the element name specifies the specific
    operation. This base type shall be extended by each specific OWS to
    include the additional required "service" attribute, with the
    correct value for that OWS.

    :ivar accept_versions: When omitted, server shall return latest
        supported version.
    :ivar sections: When omitted or not supported by server, server
        shall return complete service metadata (Capabilities) document.
    :ivar accept_formats: When omitted or not supported by server,
        server shall return service metadata document using the MIME
        type "text/xml".
    :ivar update_sequence: When omitted or not supported by server,
        server shall return latest complete service metadata document.
    """
    accept_versions: Optional[AcceptVersionsType] = field(
        default=None,
        metadata={
            "name": "AcceptVersions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    sections: Optional[SectionsType] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    accept_formats: Optional[AcceptFormatsType] = field(
        default=None,
        metadata={
            "name": "AcceptFormats",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    update_sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "updateSequence",
            "type": "Attribute",
        }
    )


@dataclass
class GetCapabilities(GetCapabilitiesType):
    class Meta:
        namespace = "http://www.opengis.net/ows"
