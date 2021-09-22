from dataclasses import dataclass
from bindings.csw_publication.envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Envelope(EnvelopeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
