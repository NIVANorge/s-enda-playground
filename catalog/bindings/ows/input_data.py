from dataclasses import dataclass
from bindings.ows.manifest_type import ManifestType

__NAMESPACE__ = "http://www.opengis.net/ows/2.0"


@dataclass
class InputData(ManifestType):
    """Input data in a XML-encoded OWS operation request, allowing including
    multiple data items with each data item either included or referenced.

    This InputData element, or an element using the ManifestType with a
    more-specific element name (TBR), shall be used whenever applicable
    within XML-encoded OWS operation requests.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/2.0"
