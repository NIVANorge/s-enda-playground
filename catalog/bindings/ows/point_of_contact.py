from dataclasses import dataclass
from bindings.ows.responsible_party_type import ResponsiblePartyType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class PointOfContact(ResponsiblePartyType):
    """Identification of, and means of communication with, person(s)
    responsible for the resource(s).

    For OWS use in the ServiceProvider section of a service metadata
    document, the optional organizationName element was removed, since
    this type is always used with the ProviderName element which
    provides that information. The optional individualName element was
    made mandatory, since either the organizationName or individualName
    element is mandatory. The mandatory "role" element was changed to
    optional, since no clear use of this information is known in the
    ServiceProvider section.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
