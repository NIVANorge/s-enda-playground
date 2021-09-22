from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.operations_metadata import OperationsMetadata
from bindings.csw_publication.service_identification import ServiceIdentification
from bindings.csw_publication.service_provider import ServiceProvider

__NAMESPACE__ = "http://www.opengis.net/ows"


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
