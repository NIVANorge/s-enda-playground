from dataclasses import dataclass, field
from typing import Optional
from bindings.csw_publication.contact_info import ContactInfo
from bindings.csw_publication.role import Role

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class ResponsiblePartyType:
    """Identification of, and means of communication with, person responsible
    for the server.

    At least one of IndividualName, OrganisationName, or PositionName
    shall be included.
    """
    individual_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    organisation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrganisationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    position_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PositionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    contact_info: Optional[ContactInfo] = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
        }
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows",
            "required": True,
        }
    )
