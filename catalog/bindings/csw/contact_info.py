from dataclasses import dataclass
from bindings.csw.contact_type import ContactType

__NAMESPACE__ = "http://www.opengis.net/ows"


@dataclass
class ContactInfo(ContactType):
    """
    Address of the responsible party.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows"
