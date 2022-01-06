from dataclasses import dataclass
from bindings.wfs.contact_type import ContactType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ContactInfo(ContactType):
    """
    Address of the responsible party.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
