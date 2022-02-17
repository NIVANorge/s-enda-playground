from dataclasses import dataclass, field
from typing import Optional
from bindings.ows.contact_info import ContactInfo
from bindings.ows.role import Role

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ResponsiblePartySubsetType:
    """Identification of, and means of communication with, person responsible
    for the server.

    For OWS use in the ServiceProvider section of a service metadata
    document, the optional organizationName element was removed, since
    this type is always used with the ProviderName element which
    provides that information. The mandatory "role" element was changed
    to optional, since no clear use of this information is known in the
    ServiceProvider section.
    """

    individual_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    position_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PositionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    contact_info: Optional[ContactInfo] = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/2.0",
        },
    )
