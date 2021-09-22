from dataclasses import dataclass
from bindings.csw_publication.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalExtent(EnvelopeType):
    """
    An interval defining the vertical spatial domain of this object.
    """
    class Meta:
        name = "verticalExtent"
        namespace = "http://www.opengis.net/gml"
