from dataclasses import dataclass, field
from typing import Optional
from bindings.ows.online_resource_type import OnlineResourceType
from bindings.ows.responsible_party_subset_type import ResponsiblePartySubsetType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ServiceProvider:
    """
    Metadata about the organization that provides this specific service
    instance or server.

    :ivar provider_name: A unique identifier for the service provider
        organization.
    :ivar provider_site: Reference to the most relevant web site of the
        service provider.
    :ivar service_contact: Information for contacting the service
        provider. The OnlineResource element within this ServiceContact
        element should not be used to reference a web site of the
        service provider.
    """
    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"

    provider_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProviderName",
            "type": "Element",
            "required": True,
        }
    )
    provider_site: Optional[OnlineResourceType] = field(
        default=None,
        metadata={
            "name": "ProviderSite",
            "type": "Element",
        }
    )
    service_contact: Optional[ResponsiblePartySubsetType] = field(
        default=None,
        metadata={
            "name": "ServiceContact",
            "type": "Element",
            "required": True,
        }
    )
