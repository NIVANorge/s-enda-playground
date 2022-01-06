from dataclasses import dataclass
from bindings.ows.contact_type import ContactType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class ContactInfo(ContactType):
    """
    Address of the responsible party.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
