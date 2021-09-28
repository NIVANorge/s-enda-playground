from dataclasses import dataclass, field
from typing import List, Optional
from bindings.wfs.code_type import CodeType
from bindings.wfs.description_type import DescriptionType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ServiceIdentification(DescriptionType):
    """General metadata for this specific server.

    This XML Schema of this section shall be the same for all OWS.

    :ivar service_type: A service type name from a registry of services.
        For example, the values of the codeSpace URI and name and code
        string may be "OGC" and "catalogue." This type name is normally
        used for machine-to-machine communication.
    :ivar service_type_version: Unordered list of one or more versions
        of this service type implemented by this server. This
        information is not adequate for version negotiation, and shall
        not be used for that purpose.
    :ivar profile: Unordered list of identifiers of Application Profiles
        that are implemented by this server. This element should be
        included for each specified application profile implemented by
        this server. The identifier value should be specified by each
        Application Profile. If this element is omitted, no meaning is
        implied.
    :ivar fees: If this element is omitted, no meaning is implied.
    :ivar access_constraints: Unordered list of access constraints
        applied to assure the protection of privacy or intellectual
        property, and any other restrictions on retrieving or using data
        from or otherwise using this server. The reserved value NONE
        (case insensitive) shall be used to mean no access constraints
        are imposed. When this element is omitted, no meaning is
        implied.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    service_type: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "required": True,
        }
    )
    service_type_version: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceTypeVersion",
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"\d+\.\d?\d\.\d?\d",
        }
    )
    profile: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
        }
    )
    fees: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Element",
        }
    )
    access_constraints: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AccessConstraints",
            "type": "Element",
        }
    )
